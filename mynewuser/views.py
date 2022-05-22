from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def clear_messages(request):
    storage = messages.get_messages(request)
    storage.used = True

def sign_in(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                clear_messages(request)
                return redirect("index")
            else:
                messages.error(request,"Неверное имя пользователя или пароль.")
        else:
            messages.error(request,"Неверное имя пользователя или пароль.")
    else:
        clear_messages(request)
    form = AuthenticationForm()

    return render(request, 'mynewuser/signin.html', context={"form":form})

def sign_up(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            clear_messages(request)
            return redirect("index")
        print(form.errors)
        for field in form.errors:
            for error in form[field].errors:
                messages.error(request, error)
    else:
        clear_messages(request)
    form = NewUserForm()

    return render(request=request, template_name="mynewuser/signup.html", context={"form": form})

def sign_out(request):
	logout(request)
	return redirect("index")
