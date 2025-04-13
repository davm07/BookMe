# Overview

Two years ago I started reading constantly and from that moment on I was enchanted with reading. I have developed this app, with the idea of giving people an opportunity to search for books that interest them. The entry point of the app shows a search bar, and 6 cards that represent genres or categories of books. By doing a search or selecting one of these genres, the user is taken to a view that shows a list of books that have a certain match with the search term or genre. The list has a pagination option, which serves to display 10 results at the same time. By clicking on the book detail link, the user is taken to a view that contains basic information about the book, such as its title, a brief description, image, publication date and number of pages.

In addition, this view has the option to add the book to a favorites list in case the user is logged in. People using the app can register to add their books to the favorites list.

To use the app, just download the repo locally, install the requirements, and run the server. The app is available at http://127.0.0.1:8000/. Run the following command to start the server:

```bash
python manage.py runserver
```

I developed this app using Python and Django, as I consider them to be interesting technologies in the world of software development. Also, I was curious to know how web app development works using Python.

It is important to mention that you need to install django to be able to use the app, you can do that with the following command:

```bash
pip install django
```

After that apply the migrations like this:

```bash
python manage.py migrate
```

[Software Demo Video](https://youtu.be/MocJrYR8IAU)

# Web Pages

1. As mentioned above, the app has an entry point which shows a search bar and 6 cards with the genres or categories of each book. When doing a search, or clicking on a category card button, the user is taken to another view, which shows the books related to the search term or genre.

2. The tab that displays the search results is basically dynamically created depending on what the user is looking for. This tab shows the title of the book, the authors, the category or genre, the date or year of publication and the cover of the book. In case one of these results is not present a default message is displayed. In addition, each book that is displayed in the results table has a link to go to the book detail view.

3. By clicking on that link in the results view, the user is taken to the book detail page. This page is also dynamically generated as it depends on the book ID. This view shows the title of the book, its authors, the date of publication, its genres or categories, a brief description, the number of pages, and its cover. Also, this view gives the option to add the book to favorites in case the user is registered and has an active session. In case the user is not logged in, a message is simply displayed to remind the user to log in to add the book to his favorites.

4. To continue the flow of the app, and add books to the favorites table in the database, it is necessary to create a user or log in. For this the app has buttons on the top page that allow you to go to these URLs. The forms shown in the app are quite easy to fill in. You need to create a username and a password. When registering and logging in, the user is immediately redirected to his profile which shows the list of his favorite books. If the user has no list, a default message is displayed. This view is also dynamically generated as it requires a user and a list of books.

5. If you want to add a book to favorites, it is necessary to go to the view that shows the details of the book. If the user is authenticated and the book is not already registered as a favorite, a button is enabled to register the book as a favorite. This action reloads the page and shows that the book has already been added to the favorites list. After that the user can return to his profile by clicking the button in the upper right corner. If there are favorite books present, they will be displayed in a masonry layout style.

6. Finally, the user can logout by clicking the logout button.

# Development Environment

- Python 3.13.0 - I used this python version to develop the app. I consider that pythos is a good language to learn and use for web development.
- Django 5.2 - I used this framework to develop the app. I believe that Django is a good framework with a lot of features and a good documentation. Also, it is easy to use and understand.
- Bootstrap 5.3.5 - I used this CSS framework to develop the app. Bootstrap helped me to create a responsive and modern design for the app. Also, it is easy to use and understand.
- VsCode - I used this IDE to develop the app.
- Google Books API - I used this API to fetch the books data from Google Books. I believe that this API is a good source of data for books. It has some limitations, but it is a good option to get the data I needed. To use this API, is not necessary to gehenerate an API key, as it is free to use. Nevertheless, if you want more advanced features, you have to generate an API key.
- SQLite - I used this database to store the data of the app. It is a lightweight database that is easy to use and understand. It is also easy to install and use.

# Useful Websites

Here are some useful websites that helped me to understand the concepts and the technologies used in this project.

- [Python Documentation](https://docs.python.org/3/index.html)
- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Django templates documentation](https://docs.djangoproject.com/en/5.2/topics/templates/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Django tutorial](https://www.youtube.com/playlist?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX) (I recommend this tutorial to learn Django)
- [Google Books API Documentation](https://developers.google.com/books/docs/v1/using)
- [Google Books API Postaman Collection](https://www.postman.com/postman/commerce-api/documentation/bnw7qeu/google-books-api) (I recommend this tool to test the API, and see the results in a more user-friendly way)
- [Django VsCode Extension](https://marketplace.visualstudio.com/items/?itemName=batisteo.vscode-django) (I recommend this extension to help you with Django development in VsCode)

# Future Work

Some ideas to improve the project:

- Give an option to remove the book from the favorites list. At the moment this is not possible and would be a very useful feature. Also, you could have a button to delete all books if necessary.
- Improve the search for books. Add a composite search that includes the normal query and genre or even year. At the moment this search is not possible and is more general.
- Incorporate JavaScript to display changes in the client without reloading the page. For example, instead of using a bookmark button that makes a post, I could use a heart icon that has an animation with the same logic of adding the bookmark book.
- Add a review section in the details of each book. The user could leave his review only if he is authenticated.
