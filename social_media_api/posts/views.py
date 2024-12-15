# posts/views.py

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404  # Correct import for get_object_or_404
from .models import Post, Like
from .serializers import PostSerializer
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """
        Allows a user to like a post.
        Creates a like if not already liked and generates a notification.
        """
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You already liked this post."}, status=400)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response({"detail": "Post liked successfully."}, status=201)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        """
        Allows a user to unlike a post.
        Removes the like and generates a notification.
        """
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        like = Like.objects.filter(post=post, user=request.user).first()
        if not like:
            return Response({"detail": "You haven't liked this post."}, status=400)

        like.delete()

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="unliked your post",
            target=post
        )

        return Response({"detail": "Post unliked successfully."}, status=200)

    @action(detail=False, methods=['get'])
    def feed(self, request):
        """
        Returns the feed for the current user, including posts from followed users.
        """
        user = request.user
        following_users = user.following.all()

        # Get posts from users the current user is following
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

