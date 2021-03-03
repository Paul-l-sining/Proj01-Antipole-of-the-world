from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker
from filestack import Client

# class is like a blueprint where you can create stuff (instances) using it.
class Geopoint(Marker):
    
    def __init__(self, latitude, longitude, popup= None ): #self is identifier
        super().__init__(location= [latitude, longitude], popup= popup)
        self.latitude = latitude
        self.longitude = longitude


    def closest_parallel(self):
        return round(self.latitude)  # latitude can't be accessed but self.latitude can
    
    def get_time_zone(self):
        timezone_string = TimezoneFinder().closest_timezone_at(lat= self.latitude, lng= self.longitude)
        return timezone_string
        
    def get_time(self):
        timezone_string = TimezoneFinder().closest_timezone_at(lat= self.latitude, lng= self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now
    
    def get_weather(self):
        weather = Weather(apikey = "f6f970013f0f39ea27a183b04c0bd0ba", lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()  # Make sure internet is connected
    
    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90, 90), longitude = uniform(-180, 180))




# shanghai = Geopoint(latitude= 31.44, longitude= 121.36) # Geopoint is a class, shanghai is an instance
# shanghai.get_time_zone()
# shanghai.closest_parallel()

# print(shanghai.latitude_range)

# print(shanghai.closest_parallel())
# print(shanghai.get_time())
# print(shanghai.get_weather())
# print(shanghai.random())