from folium import Map, Marker, Popup
from geo import Geopoint

# Get latitude and longitude values
# without using CLI 
# locations = [[31, 121], [30, 120], [12, 119]]

# using CLI

latitude = float(input ('Hey user, please enter the latitude of the place, e.g. 31.44 : '))
longitude = float(input ('Hey user, please enter the longitude of the place, e.g. 121.36 ; '))
locations = [[latitude, longitude]]

tz = Geopoint(latitude= locations[0][0], longitude= locations[0][1])
city = tz.get_time_zone().split('/')
print(f'You are nearby {city[-1]} in {city[0]}')


antipode_latitude = latitude * -1
# Add 180 for negative longtitudes
# Subtract 180 for positive longitudes
if longitude < 0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude - 180
    
locations.append([antipode_latitude, antipode_longitude])


anti_tz = Geopoint(latitude= locations[1][0], longitude= locations[1][1])
anti_city = anti_tz.get_time_zone().split('/')
print(f'The other side of world is nearby {anti_city[-1]} in {anti_city[0]}')

# Folium a map instance
# mymap = Map(location =[31.44, 121.36])
mymap = Map(location =[latitude, longitude])

for lat, lon in locations:
    # Create a Geopoint instance
    geopoint = Geopoint (latitude = lat, longitude = lon)

    forecast = geopoint.get_weather()

    # extract item using slicing method from sequence type
    popup_content= f"""
    {forecast[0][0][-8:-6]}: {round(forecast[0][1])}°F <img src= 'http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png' width = 35>
    <hr>
    {forecast[1][0][-8:-6]}: {round(forecast[1][1])}°F <img src= 'http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png' width = 35>
    <hr>
    {forecast[2][0][-8:-6]}: {round(forecast[2][1])}°F <img src= 'http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png' width = 35>
    <hr>
    {forecast[3][0][-8:-6]}: {round(forecast[3][1])}°F <img src= 'http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png' width = 35>

    """
    popup = Popup(popup_content, max_width = 400)
    popup.add_to(geopoint)

    geopoint.add_to(mymap)


# Save the Map instance into HTML file
mymap.save("Map.html")

