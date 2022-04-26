from rest_framework import generics
from .serializers import LocationSerializer, DistanceSerializer
from location_django.settings import GOOGLE_API_KEY, GOOGLE_BASE_URL
import requests
from .models import Location, Distance
from .helpers import haversine, to_kms

# Adds and returns new Location with place or address entry
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

# Adds and returns new Location with latitude, longitude entry
class ReverseLocationAdder(generics.ListCreateAPIView):
  serializer_class = LocationSerializer

  def get_queryset(self):
    searched_lat = self.kwargs['lat']
    searched_lng = self.kwargs['lng']
    query = {'latlng': searched_lat + ',' + searched_lng, 'key': GOOGLE_API_KEY}
    geocode = requests.get(GOOGLE_BASE_URL, params=query)
    geo_json = geocode.json()
    results = geo_json["results"]
    for result in results:
      if result["geometry"]["location"]["lat"] == float(searched_lat):
        if result["geometry"]["location"]["lng"] == float(searched_lng):
          result_index = results.index(result)
          break
    final_result = results[result_index]
    google_id = final_result["place_id"]
    existing_location = Location.objects.filter(google_id=google_id)
    if existing_location:
      return existing_location
    else:
      address = final_result["formatted_address"]
      latitude = final_result["geometry"]["location"]["lat"]
      longitude = final_result["geometry"]["location"]["lng"]
      new_location = Location(address=address, latitude=latitude, longitude=longitude, google_id=google_id)
      new_location.save()
      return Location.objects.filter(id=new_location.id)

# Returns distance between two locations
class DistanceFinder(generics.ListCreateAPIView):
  serializer_class = DistanceSerializer

  def get_queryset(self):
    # get starting_location info:
    starting = self.kwargs["starting"]
    starting_id = int(starting)
    starting_location = Location.objects.filter(id=starting_id).values()[0]
    starting_lat = starting_location["latitude"]
    starting_lng = starting_location["longitude"]
    # get destination info:
    ending = self.kwargs["ending"]
    ending_id = int(ending)
    ending_location = Location.objects.filter(id=ending_id).values()[0]
    ending_lat = ending_location["latitude"]
    ending_lng = ending_location["longitude"]
    # calculating distance
    total_miles = haversine(starting_lng, starting_lat, ending_lng, ending_lat)
    rounded_miles = round(total_miles, 2)
    total_kms = to_kms(total_miles)
    rounded_kms = round(total_kms, 2)
    # instantiate Location models
    starting_instance = Location(id=starting_id, address=starting_location["address"], latitude=starting_lat, longitude=starting_lng)
    destination_instance = Location(id=ending_id, address=ending_location["address"], latitude=ending_lat, longitude=ending_lng)
    # check for existing Distance
    existing_distance = Distance.objects.filter(starting_location=starting_instance).filter(destination=destination_instance)
    if existing_distance:
      return existing_distance
    else:
      # add and save Distance model instance
      new_distance = Distance(starting_location=starting_instance, destination=destination_instance, miles=rounded_miles, kilometers=rounded_kms)
      new_distance.save()
      return Distance.objects.filter(id=new_distance.id)

# View all locations
class LocationList(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

# View, update, or delete a single location
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
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
