from Location import Location
from Menu import Menu
from time import sleep

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
    l.GetWeather()
    l.RankHours()

    if m.try_again():
        m.clear()
        m.progress = 0
        continue
    else:
        break
