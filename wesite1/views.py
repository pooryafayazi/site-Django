from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return render(request, 'wesite1/index.html')

def about_view(request):
    return render(request, 'wesite1/about.html')

def contact_view(request):
    return render(request, 'wesite1/contact.html')
    #return HttpResponse('<h1>contact Page</h1>')
