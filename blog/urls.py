
from django.urls import path

from blog.views import *
#from .views import http_test, json_test

app_name = 'blog'

urlpatterns = [
    path('blog', blog_view ,name='index'),
    path('blog/single', blog_single ,name='single'),

]
