# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
 # api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]

# api/urls.py
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
