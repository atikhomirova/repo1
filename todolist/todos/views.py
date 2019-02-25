# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from todos.models import Todo  # Ant: Add full path to the module

def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context)

def details(request, id):
    #todo = Todo.objects.get(id=id)  # Ant: if id will not be valid, exception raises, so you can use https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#get-object-or-404
    todo = get_object_or_404(Todo, id=id)
    context = {'todo': todo}
    return render(request, 'details.html', context)

def add(request):
    if request.method=='POST':  # Ant: brackets is in if statement is not pythonic style
        title = request.POST.get('title')
        text = request.POST.get('text')

        if title and text:
            todo = Todo(title=title, text=text)
            todo.save()
            return redirect('/todos')
    else:
        return render(request, 'add.html')

def remove(request, id):
        #todo = Todo.objects.get(id=id)  # Ant: Same as above
        todo = get_object_or_404(Todo, id=id)
        todo.is_done = True
        todo.closed_at = datetime.now()
        todo.save()
        return redirect('/todos')
