from rest_framework import permissions

class IsTaskOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read permissions to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow owners of the task to edit/delete it
        return obj.user == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read permissions for non-authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow full permissions only to admin users
        return request.user and request.user.is_staff
