
# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Route for the function-based view
    path('books/', views.list_books, name='list_books'),

    # Route for the class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
