# pylint: disable=missing-docstring

import time
import webbrowser
import datetime
import pandas as pd
import sys
import csv
#import datetime
import calendar
import requests
from os.path import split

pd.set_option('display.width', 200)


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





def try_me():
    """ Open my social network profiles
    """
    print("*************************************")
    print("Hello world, welcome to my package...")
    time.sleep(2)
    print("******************************")
    print("The most important thing is...")
    time.sleep(2)
    print("3")
    time.sleep(2)
    print("2")
    time.sleep(2)
    print("1")
    webbrowser.open('https://www.youtube.com/watch?v=fNFzfwLM72c', new=2)
    webbrowser.open('https://www.youtube.com/watch?v=fNFzfwLM72c', new=2)
    webbrowser.open('https://www.youtube.com/watch?v=fNFzfwLM72c', new=2)
    webbrowser.open('https://www.youtube.com/watch?v=fNFzfwLM72c', new=2)
    webbrowser.open('https://www.youtube.com/watch?v=fNFzfwLM72c', new=2)
    print("**************")
    print("Ah ah ah ah...")
    time.sleep(2)
    print("***************")
    print("Staying alive!")
    print("***************")


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    # folder_source, _ = split(hello_world.__file__)
    # df = pd.read_csv('{}/data/data.csv.gz'.format(folder_source))
    # clean_data = clean_data(df)
    # print(' dataframe cleaned')
    try_me()
