from django.shortcuts import render
from Gallery.models import *


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
