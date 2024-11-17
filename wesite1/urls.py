
from django.urls import path

from wesite1.views import json_test, http_test
#from .views import http_test, json_test

urlpatterns = [
    path('http-test', http_test ),
    path('json-test', json_test )
]
