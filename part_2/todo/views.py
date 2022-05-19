from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def todolist(request):
    data = Item.objects.all()
    return render(request, "todo/home.html", {'data':data})

def impressum(request):
    return render(request, "todo/impressum.html", {})
