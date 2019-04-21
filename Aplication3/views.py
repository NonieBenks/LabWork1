from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
    return HttpResponse('<h3>This is Aplication3!</h3>')
def page_number(request , number):
    return HttpResponse('You are reading reviews page' + number)
def first_comment(request):
    return HttpResponse('First comment')
def number_comment(request, number):
    return HttpResponse('Your comment has number '+number)
def page_action(request, number, ACTION):
    if ACTION == "edit":
        return HttpResponse('You are editing page ' + number)
    elif ACTION == 'delete':
        return HttpResponse('You are deleting page ' + number)
    elif ACTION == 'answer':
        return HttpResponse('You are discussing page ' + number)
    else:
        return HttpResponse('This wrong ACTION')
