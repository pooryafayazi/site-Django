
from django.urls import path

from blog.views import *
#from .views import http_test, json_test

app_name = 'blog'

urlpatterns = [
    path('', blog_view ,name='index'),
    path('single', blog_single ,name='single'),

]
