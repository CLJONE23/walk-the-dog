# Inspiration

One rainy day I struggled to get my dog to outside. I felt terrible and vowed to take her out during the next break in the rain. Unfortunately, after looking at my weather app it was clear that there wasn't going to be a break. I wished for a quick way to determine when would be best to take her out and this application is the result.

# Purpose

Quickly determine the best time to take your four legged friend for a walk outside.

# How it works

You will enter your five digit US zip code, how many hours from now you'd like to start your walk window and finally how many hours from now your walk window will end. With this information the program will gather weather data, score that data using optimal weather conditions and then rank the scored data. Your walk window will then be presented to you in table format showing you the most optimal time to take your dog for a walk first (lowest score) and the least optimal time (highest score). The table will also include weather data for each hour/row.

# Dependencies

I believe that all dependencies other than 'requests' are installed with python 3, however if you get an error when trying to run the program ensure that all dependencies are installed.

## Needs to be installed:

- requests

Windows

```
py -m pip install requests
```

Unix/macOS

```
python -m pip install requests
```

## Should be installed:

- json
- datetime
- time
- os
- re
- operator

# Sources and API Keys

- [OpenWeather](https://openweathermap.org/) for weather data. This API requires a key. For Code Louisville, I will supply the key. Outside of Code Louisville, you will need to sign up for your own API key.
- [opendatasoft](https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/api/) for zip code to coordinates conversion. This API does not require a key.

# Steps to Run

1. Add your OpenWeather api key to the 'api_key_for_weather' variable at the top of main.py and save.
1. Run main.py

# Code Louisville Requirements Met

1. Master Loop: Menu class is designed to loop through the process asking the user for input until the user indicates they would like to quit.

1. Create a Class: This program implements four classes. There are several instances of most classes allowing and those instances are used to pass data to other classes.

1. Create a List: This program implements as list to hold several Hour objects. Those object are then sorted and rendered in the console.

1. Create and call at least three functions: There are several functions in this program, many of which retrieve, manipulate and render data.

1. Implement a regular expression: This program implements at least one regular expression to validate user input.

1. Connect to a third party API: This program retrieves data from two separate APIs and uses that data to provide the user with recommendations. Some of the data is even rendered to the console for the user.
