from Location import Location
from Menu import Menu
from time import sleep

api_key_for_weather = ''

if api_key_for_weather == '':
    print("\nYou're missing the api key for openweathermap.\nPlease update the 'api_key_for_weather' variable in main.py with a valid api key, save and relaunch.\n")
    sleep(3)
    exit
else:
    welcome_message = """

        Welcome to Walk-the-Dog where you can take the
        guesswork out of walking your furry friend.

        Stay dry and enjoy your walk.

    """
    print(welcome_message)
    sleep(3)

    m = Menu()

    while True:

        m.render()
        l = Location(m.zipcode, m.start, m.end)
        l.GetLocation()
        l.GetWeather(api_key=api_key_for_weather)
        l.RankHours()

        if m.try_again():
            m.clear()
            m.progress = 0
            continue
        else:
            break
