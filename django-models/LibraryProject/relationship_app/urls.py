from django.urls import path
from . import views  # Import your views from views.py
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Login
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # Logout
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # Register
    path('register/', views.register, name='register'),  # Include the register view
]
