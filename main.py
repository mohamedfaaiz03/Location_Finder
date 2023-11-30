import phonenumbers
import opencage
import folium
from phonenumbers import geocoder

number = input()
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

key = '58cf8e05f0de4e09b52d30a72b2bdca4'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")
