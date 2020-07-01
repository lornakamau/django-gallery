import numpy as np
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Category, Location
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    images = Image.objects.all()
    print(images[0].category)
    arr= np.array(images) 
    newarr = np.array_split(arr,3)
    first = newarr[0]
    second = newarr[1]
    third = newarr[2]
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {"first": first,"second": second,"third": third,"locations": locations,"categories": categories})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search = request.GET.get("category")
        try:
            category = Category.objects.get(name = search)
            images = Image.search_image(category)
            arr= np.array(images) 
            newarr = np.array_split(arr,3)
            first = newarr[0]
            second = newarr[1]
            third = newarr[2]
            message = f"Found {len(images)} image(s) under the category - {search}"
            return render(request, 'search.html',{"message":message,"images": images,"first": first,"second": second,"third": third})
        except ObjectDoesNotExist:
            message = "NO ITEMS UNDER CATEGORY " + search.upper()
            categories = Category.objects.all()
            return render(request, 'search.html',{"message":message, "categories": categories}) 

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

def image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        print(image.category.id)
    except ObjectDoesNotExist:
        message = "Image does not exist or may have been deleted!"
        return render(request, 'image.html', {"message":message})
    return render(request, 'image.html', {"image":image})

def category(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
        images = Image.search_image(category)
        arr= np.array(images) 
        newarr = np.array_split(arr,3)
        first = newarr[0]
        second = newarr[1]
        third = newarr[2]
        message = category.name
        title = category.name
        return render(request, 'search.html',{"title":title, "message":message,"images": images,"first": first,"second": second,"third": third})
    except ObjectDoesNotExist:
        message = "NO ITEMS UNDER CATEGORY " + search.upper()
        categories = Category.objects.all()
        title= "Not Found"
        return render(request, 'search.html',{"title":title,"message":message, "categories": categories})

def location(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
        images = Image.filter_by_location(location)
        arr= np.array(images) 
        newarr = np.array_split(arr,3)
        first = newarr[0]
        second = newarr[1]
        third = newarr[2]
        message = location.name
        title = location.name
        return render(request, 'search.html',{"title":title, "message":message,"images": images,"first": first,"second": second,"third": third})
    except ObjectDoesNotExist:
        message = "NO ITEMS FOR THAT LOCATION"
        locations = Location.objects.all()
        title= "Not Found"
        return render(request, 'search.html',{"title":title,"message":message, "locations": locations})
