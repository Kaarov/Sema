from django.conf.urls import url
from django.urls import path, include
from Gallery.views import *

# from rest_framework import routers

# app_name = 'shopping'

# router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', gallery, name='gallery'),
]
