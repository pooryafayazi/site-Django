from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
# Create your views here.


from django.contrib import messages

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_or_email = request.POST.get('username_or_email')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                user = authenticate(username=user.username, password=password)                
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have successfully logged in.')
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password.')
            else:
                messages.error(request, 'Invalid username or password.')

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