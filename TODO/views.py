from django.shortcuts import render
from django.http import HttpResponse  #4th---------------

# Create your views here.

def index(request):
    return HttpResponse("Hello, world")

def about(request):
    return HttpResponse("This is maisha")


# 4 types of function
def get():
    todo_list = TODO.objects.all()

def creat():
    TODO.objects.creat()

def update(reqest,id):
    todo = TODO.objects.get(id=id)
    todo.title = "My first project"
    todo.describtion = "My second project"
    todo.save()

    return HttpResponse(f"{todo.title} and {todo.describtion} updated")

def delete():
    pass