from django.shortcuts import render
from bs4 import BeautifulSoup
import requests as requests1
from requests.compat import quote_plus
from .models import Searchs

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://www.olx.ua/list/q-{}/'

def home(request):
    return render(request, 'base.html')

def new_searh(request):
    if request.method == "POST":
        reqw = request.POST["search"]
        Searchs.objects.create(search=reqw)
        data = requests1.get(BASE_CRAIGSLIST_URL.format(quote_plus(reqw)))
        soup = BeautifulSoup(data.text, features='html.parser')
        post_ = soup.find_all('tr',class_="wrap")

        final_post = []
        for poste in post_:
            main_q = poste.td.div.table.tbody.find_all("tr")[0].find_all("td")
            post_title = main_q[1].div.h3.a.find("strong").text
            post_url = main_q[1].div.h3.find("a")["href"]
            try:
                post_price = main_q[2].find("p", class_ = "price").text
            except:
                post_price = 'N/A'
            post_image = main_q[0].a.find("img")["src"]
            final_post.append((post_title,post_url,post_price,post_image))

        content = {
        'search': reqw,
        'final_post' : final_post,
        }
        return render(request, 'my_app/new_search.html', content)