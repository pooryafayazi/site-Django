
from django.urls import path

from wesite1.views import *
#from .views import http_test, json_test

urlpatterns = [
    path('home', index_view ),
    path('about', about_view ),
    path('contact', contact_view )
]
