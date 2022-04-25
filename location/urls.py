from django.urls import path
from . import views

urlpatterns = [
    # URL slugs for API
    path('location/<address>', views.LocationAdder.as_view(), name='location_adder'),
    path('locations/', views.LocationList.as_view(), name='location_list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
    path('distance/<starting>+<ending>', views.DistanceFinder.as_view(), name='distance_finder'),
    path('distances/', views.DistanceList.as_view(), name='distance_list'),
    path('distances/<int:pk>', views.DistanceDetail.as_view(), name='distance_detail'),
]