from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer

# Generic view to list all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Generic view to retrieve a single book by its ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Custom CreateView with data validation
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Example of custom validation: Prevent duplicate title and publication year
        title = serializer.validated_data.get('title')
        publication_year = serializer.validated_data.get('publication_year')
        if Book.objects.filter(title=title, publication_year=publication_year).exists():
            raise ValidationError("A book with this title and publication year already exists.")
        serializer.save()

# Custom UpdateView with data validation
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Example of custom behavior before saving
        instance = serializer.save()
        print(f"Book '{instance.title}' was updated.")
        
# Generic view to delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
