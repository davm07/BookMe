import requests
from functools import lru_cache

BASE_API_URL = "https://www.googleapis.com/books/v1/volumes"

@lru_cache(maxsize=1024)
def fecth_books(query, limit, offset):
    """
    This function fetches books from the Google Books API.
    It takes a query, limit, and offset as parameters.
    It returns a list of books and the total number of results.
    """
    api_url = f"{BASE_API_URL}?q={query}&maxResults={limit}&startIndex={offset}&langRestrict=en"

    response = requests.get(api_url)

    if response.status_code == 200:
        results = response.json()
        books = results.get('items', [])
        total_results = results.get('totalItems', 0)
        return books, total_results
    return [], 0

@lru_cache(maxsize=1024)
def get_book_details(book_id):
    """
    This function fetches book details from the Google Books API.
    It takes a book ID as a parameter and returns the book details as a dictionary.
    """
    api_url = f"{BASE_API_URL}/{book_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        book = response.json()
        return book
    return {}