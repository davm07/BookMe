from django.contrib import admin
from .models import FavoriteBook

class FavoriteBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book_id', 'created_at')
    search_fields = ('user__username', 'book_id')

admin.site.register(FavoriteBook, FavoriteBookAdmin)
