
from django.urls import path, include

from wesite1.views import *
#from .views import http_test, json_test

app_name = 'wesite1'

urlpatterns = [
    path('', index_view ,name='index'),
    path('about', about_view,name='about' ),
    path('contact', contact_view ,name='contact')
]
