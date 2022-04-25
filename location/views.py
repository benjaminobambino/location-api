from rest_framework import generics
from .serializers import LocationSerializer, DistanceSerializer
from location_django.settings import GOOGLE_API_KEY, GOOGLE_BASE_URL
import requests
from .models import Location, Distance
from .helpers import haversine, to_kms

# Adds and returns new Location
class LocationAdder(generics.ListCreateAPIView):
  serializer_class = LocationSerializer

  def get_queryset(self):
    searched_address = self.kwargs['address']
    query = {'address': searched_address, 'key': GOOGLE_API_KEY}
    geocode = requests.get(GOOGLE_BASE_URL, params=query)
    geo_json = geocode.json()
    results = geo_json["results"][0]
    google_id = results["place_id"]
    existing_location = Location.objects.filter(google_id=google_id)
    if existing_location:
      return existing_location
    else:
      address = results["formatted_address"]
      latitude = results["geometry"]["location"]["lat"]
      longitude = results["geometry"]["location"]["lng"]
      new_location = Location(address=address, latitude=latitude, longitude=longitude, google_id=google_id)
      new_location.save()
      return Location.objects.filter(id=new_location.id)

# View, update, or delete a single location
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

# Returns distance between two locations
class DistanceFinder(generics.ListCreateAPIView):
  serializer_class = DistanceSerializer

  def get_queryset(self):
    # getting starting_location info:
    starting = self.kwargs["starting"]
    starting_id = int(starting)
    starting_location = Location.objects.filter(id=starting_id).values()[0]
    starting_lat = starting_location["latitude"]
    starting_lng = starting_location["longitude"]
    # getting destination info:
    ending = self.kwargs["ending"]
    ending_id = int(ending)
    ending_location = Location.objects.filter(id=ending_id).values()[0]
    ending_lat = ending_location["latitude"]
    ending_lng = ending_location["longitude"]
    # calculating distance
    tot_miles = haversine(starting_lng, starting_lat, ending_lng, ending_lat)
    print(tot_miles)
    # return Distance.objects.all()

# View all locations
class LocationList(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

# View all distances
class DistanceList(generics.ListCreateAPIView):
  queryset = Distance.objects.all()
  serializer_class = DistanceSerializer

# View, update, or delete a single distance
class DistanceDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Distance.objects.all()
  serializer_class = DistanceSerializer
