from django.urls import path
from .views import list_books,register, dashboard, LibraryDetailView
from django.contrib import admin
from django.urls import path, include

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Route for the register view
    path('dashboard/', views.dashboard, name='dashboard'),  # Route for the dashboard view
]






