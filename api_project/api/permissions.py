# api/permissions.py
from rest_framework import permissions

class IsBookOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Ensure the user is the owner of the book
