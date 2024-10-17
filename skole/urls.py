from django.urls import path
from .views import sfo_elever, sfo_grupper

urlpatterns = [
    path("sfo_elever/", sfo_elever, name="sfo_elever"),
    path("sfo_grupper/", sfo_grupper, name="sfo_grupper"),
]
