from locations.location_api.location_django.settings import GOOGLE_API_KEY, GOOGLE_BASE_URL
from rest_framework import generics
from .serializers import LocationSerializer, DistanceSerializer
from .models import Location, Distance

def getLocation(apps):
  #Model variable
  Location = apps.get_model('location', 'Location')


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
