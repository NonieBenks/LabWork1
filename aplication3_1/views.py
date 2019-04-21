from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def show(request):
    return HttpResponse('<h1>aplication3_1</h1>')

def index(request):
    years = [2017, 2018, 2019, 2020, 2021]
    context = {
        'name':'Natalia',
        'lastname':'Benko',
        'job_year': years,
        "contact":{
            'nickname':'nonie',
            'phone':'380684563219',
            'email':'characteronme@gmail.com'
        },
        'date': datetime.datetime.now()


    }
    return render(request, 'index.html', context)
def condition(request):
    days=[1,2,3,4,5,6,7],
    context = {
        'current_user' : 'admin',
        'days' : days,
        'day': '4',
        'status' : "online",
        'email' : 'characteronme@gmail.com'
    }
    return render(request,'condition.html', context)
def menu(request):
    context={

    }
    return render(request,'menu.html',context)
def content(request):
    context ={

    }
    return render(request,'content.html',context)
def main(request):
    context={

    }
    return render(request,'main.html',context)
def wrapper(request):
    context={

    }
    return render(request,'wrapper.html',context)
