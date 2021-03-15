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

    def GetLocation(self):
        url = f'https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q={self.zip}&rows=1'
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            fields = data['records'][0]['fields']
            # update self with values from JSON response
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

            # create a Day object for each Day node in JSON response and store in list at self.days
            for day in data['daily']:
                # date only
                d = datetime.fromtimestamp(day['dt']).date()
                r = datetime.fromtimestamp(day['sunrise'])
                s = datetime.fromtimestamp(day['sunset'])
                self.days.append(Day(d, r, s))

            # create an Hour object for each Hour node in JSON response to falls within window
            for hour in data['hourly']:
                n = datetime.now().replace(microsecond=0, second=0, minute=0)
                # date only
                d = datetime.fromtimestamp(hour['dt'])
                r = None
                s = None

                # get hour difference between JSON response datetime and datetime.now()
                delta = d - n
                delta_to_hours = (delta.total_seconds()/60)/60

                # if delta falls within walk window, create Hour object, score and add to self.hours
                if delta_to_hours >= self.start and delta_to_hours <= self.end:
                    for day in self.days:
                        if day.date == d.date():
                            r = day.sunrise
                            s = day.sunset
                    h = Hour(hour, r, s)
                    h.Score()
                    self.hours.append(h)

    # sort hours based on their total_score, lowest to highest and render as table
    def RankHours(self):
        sorted_list = sorted(self.hours, key=operator.attrgetter(
            'total_score'))
        self.PrintResults(sorted_list)

    # render sorted list as table
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
