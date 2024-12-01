from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()
        
        # Create test data
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2002)
        
        # Set endpoints
        self.list_url = "/books/"
        self.detail_url = f"/books/{self.book1.id}/"
        
    def test_list_books(self):
        # Test unauthenticated access
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test response content
        self.assertIn("Book One", str(response.data))
        self.assertIn("Book Two", str(response.data))

    def test_create_book(self):
        self.client.login(username="testuser", password="testpassword")
        data = {"title": "Book Three", "author": "Author C", "publication_year": 2003}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        
    def test_update_book(self):
        self.client.login(username="testuser", password="testpassword")
        data = {"title": "Updated Book One", "author": "Author A", "publication_year": 2001}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")
        
    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        
    def test_filter_books(self):
        response = self.client.get(f"{self.list_url}?author=Author A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author A")
        
    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Book One", str(response.data))
        
    def test_order_books(self):
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")
