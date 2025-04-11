from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            login(request, form.save())
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("/")

    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})