import math
from django.shortcuts import render, redirect
from .utils import fecth_books, get_book_details
from urllib.parse import quote_plus
from django.contrib.auth.decorators import login_required
from .models import FavoriteBook
from django.http import HttpResponseRedirect

def books_search(request):
    """
    This function handles the books search page.
    It renders the books_search.html template and passes the request object to it.
    The view is the main entry point for the books search functionality.
    It showcases the search bar abd some static genres to search by.
    """
    return render(request, 'books_search.html')

def books_search_results(request):
    """
    This function handles the books search results page.
    It renders the results_list.html template and passes the request object to it.
    The view is the main entry point for the books search results functionality.
    It fetches the search query, limit, and page from the request object and uses them to fetch the books.
    It also calculates the total number of pages and passes them to the template.
    """
    search_query = request.GET.get('search')
    genre_query = request.GET.get('genre')
    limit = int(request.GET.get('limit', 10))
    page = int(request.GET.get('page', 1))
    offset = (page - 1) * limit

    if search_query:
        query = quote_plus(search_query)
    elif genre_query:
        query = f"subject:{quote_plus(genre_query)}"
    else:
        query = quote_plus("Jesus Christ")

    books, total_results = fecth_books(query, limit, offset)
    total_pages = math.ceil(total_results / limit) if total_results else 0

    context = {
        'title': search_query or genre_query,
        'query': search_query or genre_query,
        'books': books,
        'total_results': total_results,
        'total_pages': total_pages,
        'page': page,
        'limit': limit,
    }

    return render(request, 'results_list.html', context)

def book_detail(request, book_id):
    """
    This function handles the book detail page.
    It renders the book_detail.html template and passes the request object to it.
    The view is the main entry point for the book detail functionality.
    It fetches the book details from the Google Books API and passes them to the template.
    It also checks if the user is authenticated and if the book is in the user's favorites.
    If so, it shows a message saying that the book is already in the user's favorites.
    If not, it shows a button to add the book to the user's favorites.
    If the user is not authenticated, it shows a message saying that the user needs to login to add a book to their favorites.
    """
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = FavoriteBook.objects.filter(user=request.user, book_id=book_id).exists()
    book = get_book_details(book_id)
    return render(request, 'book_detail.html', {'book': book, 'is_favorite': is_favorite})

@login_required(login_url='/users/login/')
def add_book_to_favorites(request, book_id):
    """
    This function handles the add book to favorites functionality.
    It checks if the user is authenticated and if the book is not already in the user's favorites.
    If so, it creates a new FavoriteBook object and redirects the user to the book detail page.
    If not, it redirects the user to the book detail page.
    """
    if request.method == 'POST':
        if not FavoriteBook.objects.filter(user=request.user, book_id=book_id).exists():
            FavoriteBook.objects.create(user=request.user, book_id=book_id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect('/')