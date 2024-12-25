# Update a Book Instance

To update a book's details, first retrieve the book instance you want to update, modify its fields, and save the changes.

### Steps:
1. Open the Django shell:
   ```bash
   python manage.py shell

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
