from django.shortcuts import render
from Gallery.models import *


def gallery(request):
    category = Category.objects.all().order_by('name')
    subcategory = SubCategory.objects.all().order_by('name')
    images = Images.objects.all().order_by('name')
    context = {
        'images': images,
        'category': category,
        'subcategory': subcategory,
    }
    return render(request, 'Gallery/gallery.html', context=context)
