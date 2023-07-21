from django.shortcuts import render,HttpResponse
import requests
from datetime import datetime, timedelta

# Create your views here.

def news(request):
    API_KEY = '44220481570c4e99b633401582d605f0'
    pre_datetime =datetime.now()
    past_datetime = pre_datetime - timedelta(days=1)
    past_date = past_datetime.date()
    url = f'https://newsapi.org/v2/everything?q=movies&from={past_date}&sortBy=publishedAt&apiKey={API_KEY}'
    if request.method == 'GET':
        if request.GET.get('query') != '':
            q = request.GET.get('query')
            url = f'https://newsapi.org/v2/everything?q={q}&from={past_date}&sortBy=publishedAt&apiKey={API_KEY}'         
    response = requests.get(url)
    data = response.json()
    articles =data['articles']
    context ={
        'data':data,
        'articles' : articles,
        'key':API_KEY,
    }
    return render(request,'index.html',context)
