from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from library.models import FavoriteBook
from library.utils import get_book_details

def register_user(request):
    """
    This function handles the user registration process.
    It checks if the request method is POST and if it is, it creates a new user using the UserCreationForm.
    If the request method is not POST, it creates a new UserCreationForm instance and renders the register.html template.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("users:user_profile")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_user(request):
    """
    This function handles the user login process.
    It checks if the request method is POST and if it is, it logs the user in using the AuthenticationForm.
    If the request method is not POST, it creates a new AuthenticationForm instance and renders the login.html template.
    """
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
    """
    This function handles the user logout process.
    It logs the user out and redirects them to the login page.
    """
    if request.method == "POST":
        logout(request)
        return redirect("/")

@login_required(login_url="/users/login/")
def user_profile(request):
    """
    This function handles the user profile page.
    It checks if the user is authenticated and if they are, it renders the user_profile.html template.
    It also retrieves the user's favorite books and passes them to the template.
    """
    user = request.user
    favorite_books = FavoriteBook.objects.filter(user=user)

    my_books = []
    for book in favorite_books:
        book_id = book.book_id
        details = get_book_details(book_id)
        if details:
            my_books.append(details)

    return render(request, "users/user_profile.html", {"user": user, "my_books": my_books})
