# notifications/views.py
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Retrieve notifications for the currently authenticated user
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
