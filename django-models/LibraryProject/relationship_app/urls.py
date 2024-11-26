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

from django.urls import path
from . import views

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
