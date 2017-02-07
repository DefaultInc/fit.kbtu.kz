from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def main_view(request):
    return redirect('news_app:post_list')
