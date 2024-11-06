from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin

class IsFan(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_fan

class IsSupporter(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_supporter
