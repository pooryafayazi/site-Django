from django.shortcuts import render,HttpResponseRedirect

from wesite1.forms import ContactForm,NewsLetterForm
# Create your views here.

def index_view(request):
    #posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())[:6]
    #context = {'posts': posts}
    return render(request, 'wesite1/index.html')

def about_view(request):
    return render(request, 'wesite1/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = None
            contact.save()
            message = "your data is saved correctly"
            return render(request, 'wesite1/contact.html', {'form':form ,'message':message})
    else:
        form = ContactForm()
    return render(request, 'wesite1/contact.html')


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect("/")
    else:
         HttpResponseRedirect("/")