from django.shortcuts import render
from .models import People,Product

# Create your views here.

def home(request):
    context = {}
    return render(request, 'companyapp/home.html', context)

def products(request):
    context = {}
    context['products'] =Product.objects.all()
    return render(request, 'companyapp/products.html', context)

def people(request):
    context = {}
    context['peoples'] =People.objects.all()
    return render(request, 'companyapp/people.html', context)

def contactus(request):
    context = {}
    return render(request, 'companyapp/contactus.html', context) 
