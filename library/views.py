import math
from django.shortcuts import render
from .utils import fecth_books, get_book_details
from urllib.parse import quote_plus

def books_search(request):
    return render(request, 'books_search.html')

def books_search_results(request):
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
    book = get_book_details(book_id)
    return render(request, 'book_detail.html', {'book': book})
