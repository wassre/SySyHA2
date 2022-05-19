from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def home(response):
    list = {}
    return render(response, "todo/base.html", {})

def todolist(request):
    data = Item.objects.all()
    return render(request, "todo/home.html",{'data':data})