from django.db import models

# Create your models here.
class Location(models.Model):
  address = models.CharField(max_length=255)
  latitude = models.DecimalField(max_digits=9, decimal_places=7)
  longitude = models.DecimalField(max_digits=10, decimal_places=7)
  google_id = models.CharField(max_length=100)

  def __str__(self):
    return self.address

class Distance(models.Model):
  miles = models.DecimalField(max_digits=7, decimal_places=2)  
  kilometers = models.DecimalField(max_digits=7, decimal_places=2)  
  starting_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='distance_to_go')
  destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='distance_gone')

  def __str__(self):
    return self.miles