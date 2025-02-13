from rest_framework import permissions


class OwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
        # return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.by == request.user


class UserPermission(OwnerPermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff
