from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("profile/", views.user_profile, name="user_profile"),
]