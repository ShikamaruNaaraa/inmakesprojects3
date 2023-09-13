from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
from .models import Scrapper
def index(request):
    if request.method=='POST':
        link_name=request.POST.get('page','')
        urls=requests.get(link_name)
        beautysoup=BeautifulSoup(urls.text,'html.parser')

        for link in beautysoup.findAll('a'):
            li_address=link.get('href')
            li_name=link.string
            Scrapper.objects.create(address=li_address,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        address=Scrapper.objects.all()
    return render(request,'index.html',{'address':address})