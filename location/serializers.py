from rest_framework import serializers
from .models import Location, Distance

# Creates API readable JSON for models

class LocationSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Location
    fields = ('id', 'address', 'latitude', 'longitude')

class DistanceSerializer(serializers.HyperlinkedModelSerializer):

  starting_location = LocationSerializer(
    read_only = True
  )

  destination = LocationSerializer(
    read_only = True
  )

  class Meta:
    model = Distance
    fields = ('id', 'miles', 'kilometers', 'starting_location', 'destination')

