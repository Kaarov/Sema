from django.conf.urls import url
from django.urls import path, include
from Gallery.views import *

# from rest_framework import routers

# app_name = 'shopping'

# router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)

urlpatterns = [
    # Template
    path('category/', gallery_category, name='gallery_category'),
    path('subcategory/<int:sub>/', gallery_subcategory, name='gallery_subcategory'),
    path('image/<int:i>/', gallery_image, name="gallery_image"),


    # API
    # Category API
    path('api/v1/category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/category/<int:id>/', CategoryViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                               'put': 'update', 'delete': 'destroy'})),
    # Subcategory API
    path('api/v1/subcategory/', SubCategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/subcategory/<int:id>/', SubCategoryViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                                     'put': 'update', 'delete': 'destroy'})),

    # Product API
    path('api/v1/image/', ImageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/image/<int:id>/', ImageViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                             'put': 'update', 'delete': 'destroy'})),
]
