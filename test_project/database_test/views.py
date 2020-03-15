from django.shortcuts import render
from .models import employees 
# Create your views here.

def landingpage(request):
    context = {
        "greeting":"heylo"
    }
    return render(request, 'landingpage.html', context)

def home(request):
    context= {
        "name":"Tyler",
        "number":45
    }
    return render(request, 'home.html', context)

def datepage(request, year):
    article_list = employees.objects.filter(pub_date__year = year)
    context = {
        "year": year,
        "article_list" : article_list
    }
    return render(request, 'datepage.html', context)

def second_page(request):
    obj = employees.objects.get(id=1)
    context={
        "data":obj
    }

    return render(request, 'second_page.html', context)

def contact(request):
    return render(request, 'contacts.html')

def signuppage(request):
    return render(request, 'signup.html')