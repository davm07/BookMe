from . import views
from django.urls import path

urlpatterns = [
    path("", views.books_search, name="books_search"),
    path("books/", views.books_search_results, name="books_search_results"),
]