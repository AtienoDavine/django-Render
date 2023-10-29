
from django.shortcuts import render
#create your views here

def home(request):
    return render(request, 'home.html',  {'bike': 'home'})

def about(request):
    return render(request, 'about.html',  {'bike': 'about'})

def contact(request):
    return render(request, 'contact.html', {'bike': 'contact'})

