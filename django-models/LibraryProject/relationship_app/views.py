# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books and authors
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})  # Render the list_books template with books data

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Model associated with the view
    template_name = 'library_detail.html'  # Template to be used for rendering
    context_object_name = 'library'  # Name of the context variable to be used in the template
