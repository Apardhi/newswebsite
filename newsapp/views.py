from urllib import response
from django.shortcuts import render
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import api_view,throttle_classes

import requests
API_KEY = '698e795a81784fa1b9b4f8f282eef2f2'
# Create your views here.
@api_view(['GET'])     #decorator for function based view
@throttle_classes([UserRateThrottle])    #user request rate control
def home(request):
    '''view to sort request according to category and country'''
    category = request.GET.get('category')
    if category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
       
        url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    
    context = {'articles':articles}
    return render(request,'newsapp/home.html',context)
    
def search(request):
    '''view to provide search according to keyword provided into the searchbox'''
    search_term=request.GET['search']
    url=f'https://newsapi.org/v2/everything?q={search_term}&apiKey={API_KEY}' 
    data = requests.get(url)
    response=data.json()
    articles=response['articles']
    context={'articles':articles,'search':search_term}
    return render(request,'newsapp/search.html',context)