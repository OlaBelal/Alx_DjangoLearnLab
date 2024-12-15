# posts/views.py
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the post is created by the logged-in user
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        if Like.objects.filter(post=post, user=request.user).exists():
            return Response({"detail": "You already liked this post."}, status=400)

        Like.objects.create(post=post, user=request.user)

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
        post = get_object_or_404(Post, pk=pk)
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

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        if Like.objects.filter(post=comment.post, user=request.user).exists():
            return Response({"detail": "You already liked this comment."}, status=400)

        Like.objects.create(post=comment.post, user=request.user)

        # Create a notification for the comment's post author
        Notification.objects.create(
            recipient=comment.post.author,
            actor=request.user,
            verb="liked your comment",
            target=comment
        )

        return Response({"detail": "Comment liked successfully."}, status=201)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        like = Like.objects.filter(post=comment.post, user=request.user).first()
        if not like:
            return Response({"detail": "You haven't liked this comment."}, status=400)

        like.delete()

        # Create a notification for the comment's post author
        Notification.objects.create(
            recipient=comment.post.author,
            actor=request.user,
            verb="unliked your comment",
            target=comment
        )

        return Response({"detail": "Comment unliked successfully."}, status=200)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get notifications for the authenticated user
        return Notification.objects.filter(recipient=self.request.user)

    @action(detail=False, methods=['get'])
    def unread(self, request):
        # Fetch only unread notifications for the user
        unread_notifications = self.get_queryset().filter(is_read=False)
        serializer = self.get_serializer(unread_notifications, many=True)
        return Response(serializer.data)
