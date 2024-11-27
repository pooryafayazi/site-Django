
from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view ,name='index'),
    #path('single_', blog_single_ ,name='single_'),
    path('<str:post_id>', blog_single ,name='single'),
]
