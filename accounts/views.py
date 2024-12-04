from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #msg = f"user is authenticated as {request.user.username}"
            return redirect('/')
        #else:
            #msg = f"user is not authenticated"
    return render(request, 'accounts/login.html')

#def logout_view(request):
    

def signup_view(request):
    return render(request, 'accounts/signup.html')
