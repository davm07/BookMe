from django.db import models
from django.contrib.auth.models import User

class FavoriteBook(models.Model):
    """
    This model represents a user's favorite book.
    It has a foreign key to the User model and a CharField to store the book's ID.
    The unique_together attribute ensures that each user can only have one favorite book with a given book ID.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book_id')