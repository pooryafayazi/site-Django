from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')

def about_view(request):
    return HttpResponse('<h1>about Page</h1>')

def contact_view(request):
    return HttpResponse('<h1>contact Page</h1>')
