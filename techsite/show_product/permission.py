from rest_framework import permissions

class IsAdminOrAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD, OPTIONS запросы всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить администраторам всегда
        if request.user.is_superuser:
            return True

        # Разрешить автору комментария
        if obj.author == request.user:
            return True

        return False
