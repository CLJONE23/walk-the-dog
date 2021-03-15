import json
import requests
import re
from datetime import datetime
from Hour import Hour
from Day import Day
import operator
from time import sleep


class Location:

    def __init__(self, zip, start, end):
        self.zip = zip
        self.start = start
        self.end = end
        self.hours = list()
        self.days = list()

    def PrintDictionary(self, d):
        for k, v in d.items():
            if type(v) is dict:
                self.PrintDictionary(v)
            else:
                print(f'{k}: {v}')

    def GetLocation(self):
        url = f'https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q={self.zip}&rows=1'
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            fields = data['records'][0]['fields']
            self.longitude = fields['longitude']
            self.latitude = fields['latitude']
            self.city = fields['city']
            self.state = fields['state']

    def GetWeather(self, api_key):
        units = 'imperial'
        url = f'https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={api_key}&units={units}'

        response = requests.get(url)

        if response.status_code == 200:

            data = json.loads(response.content.decode('utf-8'))

            for day in data['daily']:
                d = datetime.fromtimestamp(day['dt']).date()
                r = datetime.fromtimestamp(day['sunrise'])
                s = datetime.fromtimestamp(day['sunset'])
                self.days.append(Day(d, r, s))

            for hour in data['hourly']:
                n = datetime.now().replace(microsecond=0, second=0, minute=0)
                d = datetime.fromtimestamp(hour['dt'])
                r = None
                s = None

                delta = d - n
                delta_to_hours = (delta.total_seconds()/60)/60

                if delta_to_hours >= self.start and delta_to_hours <= self.end:
                    for day in self.days:
                        if day.date == d.date():
                            r = day.sunrise
                            s = day.sunset
                    h = Hour(hour, r, s)
                    h.Score()
                    # print(f'(+{delta_to_hours}) {h.dt}: {h.total_score}')
                    self.hours.append(h)

    def RankHours(self):
        sorted_list = sorted(self.hours, key=operator.attrgetter(
            'total_score'))
        self.PrintResults(sorted_list)

    def PrintResults(self, slist):

        if len(slist) < 1:
            print("Sorry, no results found. Please try again.")
        else:
            h = ['Rank', 'Score', 'Date/Time', 'Description',
                 '%Rain', 'Temp(F)', 'Feels Like']

            div = '\n'
            for _ in range(101):
                div += '#'
            div += '\n'

            print(
                f'Recommendations for {self.city.capitalize()}, {self.state.upper()} ({self.zip})')
            print(div)
            print('{:<5} {:<6} {:<30} {:<30} {:<6} {:<8} {:<11}'.format(*h))
            print(div)

            i = 0
            for hour in slist:
                i += 1
                desc = hour.weather[0]['description']
                date = hour.dt.strftime('(%a) %Y-%m-%d %H:%M %Z')
                print('{:<5} {:<6} {:<30} {:<30} {:<6} {:<8} {:<11}'.format(i, hour.total_score, date,
                                                                            desc.title(), str(int(float(hour.pop)*100))+'%', hour.temp, hour.feels_like))
