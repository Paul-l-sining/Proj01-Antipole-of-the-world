from folium import Map, Marker, Popup
from geo import Geopoint

# Get latitude and longitude values

# locations = []
# for lat in range(20,40):
#     for lon in range(80,120):
#         locations.append([lat, lon])

locations = [[31.44, 121.36], [30, 120], [29, 120], [32, 120]]

# Folium a map instance
mymap = Map(location =[31.44, 121.36])

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
