from rest_framework.permissions import BasePermission

from user.models import *


class ADMINPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == ADMIN:
            return True
        else:
            return False


class TEACHERPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == TEACHER:
            return True
        else:
            return False


class STUDENTPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == STUDENT:
            return True
        else:
            return False
