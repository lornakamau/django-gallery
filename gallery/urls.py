from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(?P<image_id>\d+)',views.image,name ='image'),
    url(r'^category/(?P<category_id>\d+)',views.category,name ='category'),
    url(r'^location/(?P<location_id>\d+)',views.location,name ='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)