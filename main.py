import requests
import json
from datetime import datetime
# collect details
#  dog's name
#  zip code where your dog likes to walk
#  availability
#  duration

'''
while True:
    try:
        if input("What would you like to do?") == "q":
            print("You have selected to quit the program.")
            break
        else:
            print("You're still in the loop.")
    except:
        break

print("You're out of the loop.")
'''

# move to weatherdata class

appid = 'insert token here'
lat = '38.411964'
lon = '-85.57066'
units = 'imperial'
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={appid}&units={units}'

response = requests.get(url)

if response.status_code == 200:
    print("Data returned successfully")
    data = json.loads(response.content.decode('utf-8'))
    for hour in data['hourly']:
        m = hour['dt']
        ms = datetime.fromtimestamp(m).strftime('%Y-%m-%d %H:%M:%S')
        print(m)
        print(ms)

# get weather data
# analyze and return recommendations
