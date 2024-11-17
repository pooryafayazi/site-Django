from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('<h1>http_test OK!</h1>')

def json_test(request):
    return JsonResponse({"brand": "Ford",  "model": "Mustang",  "year": 1964})