from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
# Create your views here.

def index_view(request):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())[:6]
    context = {'posts': posts}
    return render(request, 'wesite1/index.html',context)

def about_view(request):
    return render(request, 'wesite1/about.html')

def contact_view(request):
    return render(request, 'wesite1/contact.html')
    #return HttpResponse('<h1>contact Page</h1>')
