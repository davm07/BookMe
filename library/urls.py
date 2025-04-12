from . import views
from django.urls import path

urlpatterns = [
    path("", views.books_search, name="books_search"),
    path("books/", views.books_search_results, name="books_search_results"),
    path("book/detail/<str:book_id>/", views.book_detail, name="book_detail"),
    path("book/add_favorite/<str:book_id>/", views.add_book_to_favorites, name="add_book_to_favorites"),
]