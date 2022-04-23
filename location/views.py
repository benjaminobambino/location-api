# from urllib import request
from locations.location_api.location_django.settings import GOOGLE_API_KEY, GOOGLE_BASE_URL
from rest_framework import generics
from .serializers import LocationSerializer, DistanceSerializer
from .models import Location, Distance
import requests

def getLocation(request, apps):
  #Model variable
  Location = apps.get_model('location', 'Location')
  searched_address = request.kwargs['address']
  query = {'address': searched_address, 'key': GOOGLE_API_KEY}
  geocode = requests.get(GOOGLE_BASE_URL, params=query)
  address = geocode.results.formatted_address
  latitude = geocode.results.geometry.location.lat
  longitude = geocode.results.geometry.location.lng
  newLocation = Location(address=address, latitude=latitude, longitude=longitude)
  newLocation.save()
  return newLocation


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
