from rest_framework import permissions
from .models import Enrollment


class IsClassTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        classroom = getattr(obj, "classroom", obj)
        return classroom.teacher_id == request.user.id


class IsClassMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        classroom = getattr(obj, "classroom", obj)
        return (
            classroom.teacher_id == request.user.id
            or Enrollment.objects.filter(
                user=request.user, classroom=classroom
            ).exists()
        )
