from math import radians, cos, sin, asin, sqrt

def haversine(start_lng, start_lat, end_lng, end_lat):
    # converts decimals to radians
    start_lng, start_lat, end_lng, end_lat = map(radians, [start_lng, start_lat, end_lng, end_lat])

    # Haversine formula 
    lng_dist = end_lng - start_lng 
    lat_dist = end_lat - start_lat 
    a = sin(lat_dist/2)**2 + cos(start_lat) * cos(end_lat) * sin(lng_dist/2)**2
    c = 2 * asin(sqrt(a)) 
    earth_radius = 3959.87433
    miles = c * earth_radius
    return miles

def to_kms(miles):
    kms = miles * 1.609344
    return kms