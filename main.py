import phonenumbers #pip install phonenumbers
import folium #pip install folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

number = input('Input Phone Number ( With Country Code , Example: +112341234) : ')
scrapnum = phonenumbers.parse(number)
location = geocoder.description_for_number(scrapnum, 'en') 
key = 'e7c06e5349474353b912015b53acd779'
geocode = OpenCageGeocode(key)
query = str(location)
res = geocode.geocode(query)
lat = res[0]['geometry']['lat']
lng = res[0]['geometry']['lng']
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save('location.html')

print(scrapnum)
print(location)
print(carrier.name_for_number(scrapnum, 'en'))
print(lat, lng)
