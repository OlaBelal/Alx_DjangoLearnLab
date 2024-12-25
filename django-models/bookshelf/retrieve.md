# Retrieve a Book Instance

To retrieve a book instance from the database, use the `Book.objects.get()` method to find a specific book by a unique field (e.g., `title`).

### Steps:
1. Open the Django shell:
   ```bash
   python manage.py shell
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book)
