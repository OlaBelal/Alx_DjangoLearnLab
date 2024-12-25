# Create a Book Instance

To create a book instance in Django, use the `Book.objects.create()` method. This will add a new book to the database with the specified attributes.

### Steps:
1. Open the Django shell:
   ```bash
   python manage.py shell

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
