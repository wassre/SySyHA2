from django.shortcuts import render, redirect
from .models import Item
from .forms import addItem

def todolist(response):
    data = Item.objects.all()
    return render(response, "todo/home.html", {'data':data})

def impressum(response):
    return render(response, "todo/impressum.html", {})

def new(response):
    if response.method == "POST":
        form = addItem(response.POST)
        if form.is_valid():
            t = form.cleaned_data["task"]
            d = form.cleaned_data["deadline"]
            p = form.cleaned_data["progress"]
            i = Item(task=t, deadline=d, progress=p)
            i.save()
        return redirect('')
    else:
        form = addItem()
    return render(response, 'todo/new.html', {"form":form})

def edit(request, id):
    if request.method == "GET":
        item = Item.objects.get(id=id)
        form = addItem(instance=item)
        if form.is_valid():
            item.task = form.cleaned_data["task"]
            item.deadline = form.cleaned_data["deadline"]
            item.progress = form.cleaned_data["progress"]
            item.save()
        return render(request, "todo/edit.html", {'form': form})
    else:
        item = Item.objects.get(id=id)
        form = addItem(request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('')

def delete(request, pk):
    list = Item.objects.get(id=pk)
    if request.method == 'GET':
        list.delete()
        return redirect('/')
    return render(request, '', {'item':list})
