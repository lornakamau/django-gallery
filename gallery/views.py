from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images": images})