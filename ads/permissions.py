from rest_framework.permissions import BasePermission

from users.models import User


class IsOwnerOrStaff(BasePermission):
    message = "Delete or update ads can owners or admins only."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [User.ADMIN, User.MODERATOR]:
            return True
        return False
