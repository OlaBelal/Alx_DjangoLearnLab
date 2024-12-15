from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from .models import Post, Like
from notifications.models import Notification


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



# posts/views.py


User = get_user_model()

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user

    # Prevent a user from liking a post more than once
    if Like.objects.filter(post=post, user=user).exists():
        return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create the like
    like = Like.objects.create(post=post, user=user)

    # Create a notification for the post author
    notification = Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked',
        target=post
    )

    return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def unlike_post(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user

    # Check if the user has liked the post
    like = Like.objects.filter(post=post, user=user).first()
    if not like:
        return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Remove the like
    like.delete()

    # Optionally, create a notification for the post author about the unliking
    # You can customize this further
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='unliked',
        target=post
    )

    return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
