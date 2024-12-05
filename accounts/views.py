from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_or_email = request.POST.get('username_or_email')
            password = request.POST.get('password')
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
            except:
                username = username_or_email
            user = authenticate(username=username, password=password)

            form = AuthenticationForm(request=request, data=request.POST)
            if user is not None:
                login(request, user)
                return redirect('/')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        return render(request, 'accounts/login.html' ) 
    return redirect('/')

'''
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
'''

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():                
                form.save()
                return redirect('accounts:login')  # Redirect to login page after signup
            else:
                return render(request, 'accounts/signup.html', {'form': form})  # Show form with errors
        else:
            form = CustomUserCreationForm()  # Use the custom form here
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        return redirect('/')