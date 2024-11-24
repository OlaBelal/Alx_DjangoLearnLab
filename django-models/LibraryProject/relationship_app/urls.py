from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),

    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Login
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # Logout
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # Registration
    path('register/', register, name='register'),
]
