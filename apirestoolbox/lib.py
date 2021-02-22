# pylint: disable=missing-docstring

import sys
import csv
#import datetime
import calendar
import requests


from apirestoolbox.weather import search_city

BASE_URI = "https://www.metaweather.com"
#/api/location/(woeid)/(date)/


def daily_forecast(woeid, year, month, day):
    url = f"{BASE_URI}/api/location/{woeid}/{year}/{month}/{day}"
    response = requests.get(url).json()
    #import ipdb; ipdb.set_trace()

    if response and len(response) > 0:
        return response
    return None


def monthly_forecast(woeid, year, month):
    forecasts = []
    #import ipdb; ipdb.set_trace()
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        forecasts = forecasts + daily_forecast(woeid, year, month, day)
    return forecasts

