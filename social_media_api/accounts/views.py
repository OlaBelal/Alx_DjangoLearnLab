from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from .models import CustomUser

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = request.user
        try:
            follow_user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        user.following.add(follow_user)
        return Response({"detail": "Following user"}, status=200)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = request.user
        try:
            unfollow_user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        user.following.remove(unfollow_user)
        return Response({"detail": "Unfollowed user"}, status=200)

# To get the list of users a person is following
class FollowingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.following.all()

# To get the list of followers of a user
class FollowersListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.followers_set.all()

