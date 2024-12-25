# Delete a Book Instance

To delete a book instance from the database, follow these steps:

### Steps:
1. Open the Django shell:
   ```bash
   python manage.py shell
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.delete()
Book.objects.all()
