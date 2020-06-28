import numpy as np
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Category
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    images = Image.objects.all()
    arr= np.array(images) 
    newarr = np.array_split(arr,3)
    first = newarr[0]
    second = newarr[1]
    third = newarr[2]
    return render(request, 'home.html', {"first": first,"second": second,"third": third })

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search = request.GET.get("category")
        print(search)
        try:
            category = Category.objects.get(name = search)
            images = Image.search_image(category)
            arr= np.array(images) 
            newarr = np.array_split(arr,3)
            first = newarr[0]
            second = newarr[1]
            third = newarr[2]
            message = f"{search}"
            return render(request, 'search.html',{"message":message,"images": images,"first": first,"second": second,"third": third})
        except ObjectDoesNotExist:
            message = "NO ITEMS UNDER CATEGORY: " + search.upper()
            return render(request, 'search.html',{"message":message}) 

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})