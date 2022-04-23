from django.urls import path
from . import views

urlpatterns = [
    # URL slugs for API
    path('location/<address>', views.LocationAdder.as_view(), name='location_list'),
    # path('colors/<int:pk>', views.ColorDetail.as_view(), name='color_detail'),
    # path('swatches/', views.SwatchList.as_view(), name='swatch_list'),
    # path('swatches/<int:pk>', views.SwatchDetail.as_view(), name='swatch_detail'),
]