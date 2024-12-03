from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import messages
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
            contact.name = 'Unknown'
            contact.save()
            messages.add_message(request, messages.SUCCESS ,"Your data is saved correctly") 
            return render(request, 'wesite1/contact.html', {'form':form })
        else:
            messages.add_message(request, messages.ERROR, "Your data is NOT saved!", {'form':form }) 

    else:
        form = ContactForm()
    return render(request, 'wesite1/contact.html', {'form':form })


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS ,"Your email is saved successfully")
            return HttpResponseRedirect('/')
        else:
            return render(request, 'wesite1/index.html', {'form': form}) 
    else:
        form = NewsLetterForm() 
        return render(request, 'wesite1/index.html', {'form': form})