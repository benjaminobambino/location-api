from rest_framework import serializers
from .models import Location, Distance

# Creates API readable JSON for models

class LocationSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Location
    fields = ('id', 'address', 'latitude', 'longitude')

class DistanceSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Distance
    fields = ('id', 'starting_location', 'destination', 'distance')

