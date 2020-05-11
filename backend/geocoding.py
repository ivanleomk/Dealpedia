import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((1.374616, 103.845441))
data = reverse_geocode_result



def encode_using_lat_long(data):
    lat_long = data['information']['restaurant_address']
    lat_long = (int(lat_long[0],int(lat_long[1])))
    
    data = gmaps.reverse_geocode(lat_long)
    postal_code = data[0]['address_components'][-1]['long_name']
    formatted_address = data[0]['formatted_address']
    neighbourhood = data[0]['address_components'][2]['long_name']

    address = {
        "postal_code":postal_code,
        "address": formatted_address,
        "neighbourhood": neighbourhood,
        "lat-long": lat_long
    }

    return lat_long

