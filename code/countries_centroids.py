from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd


# function to find the coordinate
# of a given city
def find_geocode(city):
    try:
        # Specify the user_agent as your
        # app name it should not be none
        geolocator = Nominatim(user_agent="your_app_name")
        return geolocator.geocode(city)
    except GeocoderTimedOut:
        return None


loc = find_geocode('italy')
print(loc.latitude)
print(loc.longitude)