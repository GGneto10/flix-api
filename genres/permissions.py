from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
       return True  # Allow all users to access the view



