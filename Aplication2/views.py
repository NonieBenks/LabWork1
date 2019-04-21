from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    return HttpResponse("<h3>This is Aplication3!</h3>")

def year(request):
    return HttpResponse("It`s current year")

def number(request , year):
    return HttpResponse("It’s year basic folder<br>"+"Year is " + year)
def month(request, year, month):
    if month<="12": return HttpResponse("It’s months basic folder<br>"+"Month is " + month)
    else: return HttpResponse("It is not current month")

def day(request, year, month, day):
    if month<="12" and day<="31": return HttpResponse("It’s days basic folder<br>"+"Month is " + month + "<br>" +"Day is" + day)
    else: return HttpResponse("It is not current day")

def argument(request, argument):
    return HttpResponse("Your argument is " + argument)
def productNum(request, number):
    if number == "1":
        return HttpResponse("First product page")
    else:
        return HttpResponse("product page with number" + number)
def folder(request):
    return HttpResponse("First product page")
