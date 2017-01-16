from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if (request.method == "GET"):
        return render(request, 'authorization_app/login.html')

    email = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    return render(request, 'authorization_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
