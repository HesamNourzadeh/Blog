import requests
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm , EditForm

def user_register(request):
    context = {'errors' : []}
    if request.user.is_authenticated:
        return redirect("home_app:homepage")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("pass1")
        password2 = request.POST.get("pass2")
        if password1 != password2:
            context['errors'].append("پسورد ها باهم برابر نیست")
            return render(request, "account_app/register.html" , context)
        user =  User.objects.create_user(username=username , password=password1 , email=email)
        login(request , user )
        return redirect("/")
    return render(request , "account_app/register.html")
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:homepage')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request , user)
            return redirect('home_app:homepage')
    else:
        form = LoginForm()

    return render(request , "account_app/login.html" , {'form' : form })

def user_edit(request):
    if request.user.is_authenticated:
        user = request.user
        form = EditForm(instance=user)
        if request.method == "POST":
          form = EditForm( instance=user , data =request.POST)
        if form.is_valid():
            form.save()
    else:
        return redirect('home_app:homepage')
    return render(request , 'account_app/edit_user.html' , {'form' : form})
def user_logout(request):
    logout(request)
    return redirect("home_app:homepage")