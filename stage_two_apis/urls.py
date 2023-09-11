from django.urls import path
from .views import ZuriEndpoints, ZuriEndpointsForRetrieveUpdateDelete

urlpatterns = [
    path("api", ZuriEndpoints.as_view(), name="zuriendpoints"),
    path("api/<int:pk>", ZuriEndpointsForRetrieveUpdateDelete.as_view(), name="zuriretrieveupdatedelete"),
]
