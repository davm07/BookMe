from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    # Route for the user registration page
    path("register/", views.register_user, name="register_user"),
    # Route for the user login page
    path("login/", views.login_user, name="login_user"),
    # Route for the user logout page
    path("logout/", views.logout_user, name="logout_user"),
    # Route for the user profile page
    path("profile/", views.user_profile, name="user_profile"),
]