from . import views
from django.urls import path


urlpatterns = [
    # Route for the books search page
    path("", views.books_search, name="books_search"),
    # Route for the books search results page
    path("books/", views.books_search_results, name="books_search_results"),
    # Route for the book detail page
    path("book/detail/<str:book_id>/", views.book_detail, name="book_detail"),
    # Route for adding a book to the user's favorites
    path("book/add_favorite/<str:book_id>/", views.add_book_to_favorites, name="add_book_to_favorites"),
]