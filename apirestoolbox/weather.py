# pylint: disable=missing-docstring

import sys
#import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    url = f"{BASE_URI}/api/location/search/"
    response = requests.get(url, params={'query': query}).json()
    if response:
      #import ipdb; ipdb.set_trace()
        return response[0]
    return None
