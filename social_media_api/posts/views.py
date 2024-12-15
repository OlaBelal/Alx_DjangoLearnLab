from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer

# This view will return the posts from users that the current user follows.
class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get the current authenticated user
        user = self.request.user

        # Get the list of users that the current user is following
        following_users = user.following.all()

        # Fetch posts from users that the current user is following, ordered by creation date (most recent first)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

