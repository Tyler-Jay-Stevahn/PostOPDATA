from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def DB(request):
    return HttpResponse('this is the latest news')

def second_page(request):
    return HttpResponse('this is also the latest new news')

def contact(request):
    return HttpResponse('this is contact page')