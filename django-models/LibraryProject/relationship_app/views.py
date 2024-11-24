# relationship_app/views.py
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})
# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # The name of the variable passed to the template

    # Optional: You can override the get_context_data method to add additional context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add more data to the context if needed
        return context

# relationship_app/views.py
from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
