from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    if (request.method == "GET"):
        return render(request, 'auth_app/login.html')
    email = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    return redirect('auth_app:login')


def logout_view(request):
    logout(request)
    return redirect('/')
