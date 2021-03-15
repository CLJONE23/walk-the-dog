# Inspiration

One rainy day I struggled to get my dog to outside. I felt terrible and vowed to take her out during the next break in the rain. Unfortunately, after looking at my weather app it was clear that there wasn't going to be a break. I wished for a quick way to determine when would be best to take her out and this application is the result.

# Purpose

Quickly determine the best time to take your four legged friend for a walk outside.

# Dependencies

I believe all of these dependicies are available with Python3 but if you have trouble with the app, please check that these dependencies are installed on your machine.

- requests
- json
- datetime
- time
- os
- re
- operator

# Sources and API Keys

- [OpenWeather](https://openweathermap.org/) for weather data. This API requires a key. For Code Louisville, I will supply the key. Outside of Code Louisville, you will need to sign up for your own API key.
- [opendatasoft](https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/api/) for zip code to coordinates conversion. This API does not require a key.

# Steps

1. Add your OpenWeather api key to the 'api_key_for_weather' variable at the top of main.py and save.
1. Run main.py
