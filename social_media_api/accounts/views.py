from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# User list and detail views
class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()  # All users
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

# Follow and Unfollow Views
@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = CustomUser.objects.get(id=user_id)
    request.user.following.add(user_to_follow)  # Add to the current user's following list
    return Response({"message": f"You are now following {user_to_follow.username}"})

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = CustomUser.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)  # Remove from following list
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}"})

# Feed View - Posts from followed users
class FeedView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the posts from followed users
        user = self.request.user
        followed_users = user.following.all()  # Get the users the current user is following
        return followed_users.posts.all()  # Assuming that posts are linked with the user

