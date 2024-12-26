from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable search functionality on the title and author fields
    search_fields = ('title', 'author')

    # Add filters to the admin interface (e.g., by publication year)
    list_filter = ('publication_year',)

# Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)
