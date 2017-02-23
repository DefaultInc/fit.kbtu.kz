from django.shortcuts import render, redirect
from auth_app.admin import UserCreationForm as UserForm

def register(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    return render(request, 'auth_app/registration.html', {'form': UserForm()})

