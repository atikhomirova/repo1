# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Ant: You don't need to use this import

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo  # Ant: Add full path to the module

def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)  # Ant: if id will not be valid, exception raises, so you can use https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#get-object-or-404
    context = {'todo': todo}
    return render(request, 'details.html', context)

def add(request):
    if(request.method=='POST'):  # Ant: brackets is in if statement is not pythonic style
        title = request.POST['title']  # Ant: if request will not have this args, exception raises
        text = request.POST['text']  # Ant: Same as above

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')

def remove(request, id):
        todo = Todo.objects.get(id=id)  # Ant: Same as above
        todo.is_done = True
        todo.save()
        #context = {'todos': todos}
        return redirect('/todos')
