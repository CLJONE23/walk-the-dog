import json
import requests


class WeatherData:

    def __init__(self, zip):
        # add type checking and validation 5
        self.zip = zip
