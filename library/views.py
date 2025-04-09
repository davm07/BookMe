import requests
import math
from django.shortcuts import render


BASE_API_URL = "https://openlibrary.org/"

def books_search(request):
    return render(request, 'books_search.html')

def books_search_results(request):
    search_query = request.GET.get('search')
    genre_query = request.GET.get('genre')
    limit = int(request.GET.get('limit', 10))
    page = int(request.GET.get('page', 1))

    offset = (page - 1) * limit
    api_url = f"{BASE_API_URL}search.json?q={search_query or genre_query}&limit={limit}&offset={offset}"

    response = requests.get(api_url)

    if response.status_code == 200:
        results = response.json()
        total_results = results.get('numFound', 0)
        books = results.get('docs', [])
        total_pages = math.ceil(total_results / limit)

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