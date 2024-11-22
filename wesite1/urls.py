
from django.urls import path

from wesite1.views import *
#from .views import http_test, json_test

urlpatterns = [
    path('', index_view ),
    path('about.html', about_view ),
    path('contact.html', contact_view )
]
