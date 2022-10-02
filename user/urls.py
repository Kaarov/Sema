from django.urls import path, include
from user.views import *

urlpatterns = [
    path("home/", home, name="home")
]
