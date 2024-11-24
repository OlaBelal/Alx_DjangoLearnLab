# relationship_app/views.py

from django.shortcuts import render
from relationship_app.models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})
# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Library

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Use the specified template for rendering
    context_object_name = 'library'  # Set the context object name to 'library' for the template
