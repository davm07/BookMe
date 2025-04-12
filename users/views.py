from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from library.models import FavoriteBook
from library.utils import get_book_details

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("users:user_profile")

    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")

@login_required(login_url="/users/login/")
def user_profile(request):
    user = request.user
    favorite_books = FavoriteBook.objects.filter(user=user)

    my_books = []
    for book in favorite_books:
        book_id = book.book_id
        details = get_book_details(book_id)
        if details:
            my_books.append(details)

    return render(request, "users/user_profile.html", {"user": user, "my_books": my_books})
