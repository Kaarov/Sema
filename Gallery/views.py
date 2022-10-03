from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from Gallery.models import *
from Gallery.serializers import *

from user.permissions import *
from rest_framework.response import Response


# Templates


def gallery_category(request):
    category = Category.objects.all().order_by('name')
    context = {
        'category': category,
    }
    return render(request, 'Gallery/gallery_category.html', context=context)


def gallery_subcategory(request, sub):
    subcategory = SubCategory.objects.filter(category__id=sub)
    return render(request, 'Gallery/gallery_subcategory.html', context={
        'subcategory': subcategory,
    })


def gallery_image(request, i):
    image = Images.objects.filter(subcategory_id=i)
    return render(request, 'Gallery/gallery_subcategory.html', context={
        'image': image,
    })


# API


# Category
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'create', 'update', 'delete']:
            self.permission_classes = [IsAuthenticated & (ADMINPermission | TEACHERPermission)]
        else:
            self.permission_classes = [IsAuthenticated & TEACHERPermission]
        return super(CategoryViewSet, self).get_permissions()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         self.serializer_class = CategoryDetailSerializer
    #     else:
    #         self.serializer_class = CategorySerializer
    #     return super(CategoryViewSet, self).get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Category.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Category.objects.get(pk=kwargs.get('id'))
            serializer = CategorySerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Category.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Category.objects.get(pk=kwargs.get('id'))
            serializer = CategorySerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Category.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Category.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------


# Subcategory
class SubCategoryViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [IsAuthenticated & (ADMINPermission | TEACHERPermission)]
        else:
            self.permission_classes = [IsAuthenticated & TEACHERPermission]
        return super(SubCategoryViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = SubCategory.objects.all()
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = SubCategory.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = SubCategory.objects.get(pk=kwargs.get('id'))
            serializer = SubCategorySerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = SubCategory.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = SubCategory.objects.get(pk=kwargs.get('id'))
            serializer = SubCategorySerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = SubCategory.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = SubCategory.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------


# Product
class ImageViewSet(ModelViewSet):
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [IsAuthenticated & (ADMINPermission | TEACHERPermission)]
        else:
            self.permission_classes = [IsAuthenticated & TEACHERPermission]
        return super(ImageViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = Images.objects.all()
        serializer = ImagesSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Images.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Images.objects.get(pk=kwargs.get('id'))
            serializer = ImagesSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Images.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Images.objects.get(pk=kwargs.get('id'))
            serializer = ImagesSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Images.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Images.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)
