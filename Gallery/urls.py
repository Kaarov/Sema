from django.conf.urls import url
from django.urls import path, include
from Gallery.views import *

# from rest_framework import routers

# app_name = 'shopping'

# router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('category/', gallery_category, name='gallery_category'),
    path('subcategory/<int:sub>/', gallery_subcategory, name='gallery_subcategory'),
    path('image/<int:i>/', gallery_image, name="gallery_image"),
]
