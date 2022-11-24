from rest_framework.permissions import BasePermission


class SelectionEditPermission(BasePermission):
    message = "Editing selections for non-owners is not allowed."

    def has_object_permission(self, request, view, obj):
        print(request.user)
        print(obj.owner)
        if request.user == obj.owner:
            return True
        return False
