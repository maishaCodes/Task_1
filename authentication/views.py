from django.shortcuts import redirect,render
from django.contrib.auth import logout
# Create your views here.

from .form import RegistrationForm

from django.contrib.auth import messages

def register(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user created successfully")
            return redirect("regform")
        
        messages.error(request,form.errors)
        return redirect("regform")
    
    else:
        form = RegistrationForm()
        context = {
            "form": form
        }

        return render(request,"registration.html",context)
    
def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request,user)
        