# As-the-Crow-Flies Location API
## Date: 4/25/2022
### By: Benjamin Peck
#### [GitHub](https://github.com/benjaminobambino) | [LinkedIn](https://www.linkedin.com/in/benjaminlpeck/)
***
### ***Description***
#### ***As the Crow Flies*** is a Google Maps API-based backend that provides endpoints to:
1. Return an address, latitude, and longitude for a place or address input.
2. Return an address, latitude, and longitude for a latitude-longitude input.
3. Last, but not least, return a distance (as the crow flies) between two locations.
***
### ***Technologies Used***
* Django
* Python
  * Requests Library
* Google Maps APIs
* SQL
***
### ***Getting Started***
#### The project backend REST API has been deployed on Heroku. Here are the URL and enpoints needed to use the API:
### Base URL
- https://locationdb-api.herokuapp.com/
### Primary Endpoints
- location/\<address>
  - Retrieves a location by place name or address.
  - Returns ID, address, latitude, and longitude.
- reverselocation/\<latitude>/\<longitude>
  - Retrieves a location by latitude-longitude.
  - Returns ID, address, latitude, and longitude.
- distance/\<starting-location-id>/\<destination-id>
  - Retrieves the distance between two locations (using the returned IDs from the location calls).
  - Returns the distance in miles and kilometers along with each location's data (ID, address, latitude, and longitude).
### Other Endpoints
- locations/
  - Returns data for all previously queried locations.
- locations/\<location-id>
  - Returns data for a specific, previously queried location based on ID.
- distances/
  - Returns data for all previously queried distances.
- distances/\<distance-id>
  - Returns data for a specific, previously queried distances based on ID.
***
### ***Future Updates***
- [ ] Add multi-point triangulation
***
### ***Resources***
- ##### [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding)
- ##### [Django Docs](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/)
- ##### [Requests Library Docs](https://docs.python-requests.org/en/latest/)
- ##### [Haversine Formula](https://newbedev.com/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)
