from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Fetch author
    books = Book.objects.filter(author=author)  # Fetch books by the author
    return books

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # Fetch library
    return library.books.all()  # Fetch books associated with the library

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Fetch library
    librarian = Librarian.objects.get(library=library)  # Fetch librarian linked to the library
    return librarian
