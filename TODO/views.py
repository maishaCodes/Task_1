from django.shortcuts import render, redirect
from django.http import HttpResponse  #4th---------------
from .models import TODO
# Create your views here.

def index(request):
    return HttpResponse("Hello, world")

# def about(request):
#     return HttpResponse("This is maisha")


def creat(request):
    if request.method == "POST":
      title = request.POST.get("title")
      description = request.POST.get("description")
      print(title, description)
      data = TODO(title=title, description=description)
      data.save()
      print("Data is saved successfully")
      return redirect("get-all")
    return render(request,"add-items.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def get_all(request):
    print("request", request)
    todo_list = TODO.objects.all().order_by("-creat_at")
    context = {
        "data": todo_list,
        "html_title" : "Items page"
    }
    return render(request, "home.html",context)

def update(request, id, title, description):
    todo = TODO.objects.get(id=id)
    todo.title = title
    todo.description = description
    todo.save
    return render(request, "update.html")

def delete(request):
    return render("request", "delete.html")    

def item(request):
    return render("request", "item.html")   


def get_data_by_id(request,id):
    print("request",request)

    todo_list = TODO.objects.get(id=id)

    context = {
        "items": todo_list,
        "html_title" : "Items page"
    }
    return render(request, "view_items.html", context)





# 4 types of function
"""
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
"""   