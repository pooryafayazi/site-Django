
from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view ,name='index'),
    path('single_', blog_single_ ,name='single_'),
    path('single/<str:post_title>/', blog_single ,name='single'),
]
