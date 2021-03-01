from Location import Location
from Menu import Menu
from time import sleep

welcome_message = """

    Welcome to Walk-the-Dog where you can take the
    guesswork out of walking your furry friend.

    Stay dry and enjoy your walk.

"""
print(welcome_message)
sleep(5)

m = Menu()
m.render()

l = Location(m.zipcode, m.start, m.end)
l.GetLocation()
l.GetWeather()
