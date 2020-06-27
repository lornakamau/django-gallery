from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images": images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        images = Image.search_image(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})