from django.shortcuts import render, redirect
from .models import employees, registrationdata 
from .forms import registration_forms
from .functions import to_dataframe
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

    context = {
        "form":registration_forms
    }

    return render(request, 'signup.html', context)


def adduser(request):
    form = registration_forms(request.POST)
    if form.is_valid():
        myregister = registrationdata(username = form.cleaned_data['username'], 
                                    password = form.cleaned_data['password'], 
                                    email = form.cleaned_data['email'], 
                                    phone = form.cleaned_data['phone'])
        myregister.save()
        return redirect('home')