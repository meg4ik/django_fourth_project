from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def home(request):
    return render(request, 'base.html')

def new_searh(request):
    reqw = request.POST.get("search")
    content = {'search': reqw,}
    return render(request, 'my_app/new_search.html', content)