from rest_framework.permissions import BasePermission
from .models import Enrollment
from django.contrib.auth.models import AnonymousUser


class IsClassTeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Swagger / schema safe
        if not obj or isinstance(request.user, AnonymousUser):
            return True

        classroom = getattr(obj, "classroom", obj)

        # safety check
        if not hasattr(classroom, "teacher_id"):
            return False

        return classroom.teacher_id == request.user.id


class IsClassMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Swagger / schema safe
        if not obj or isinstance(request.user, AnonymousUser):
            return True

        classroom = getattr(obj, "classroom", obj)

        if not hasattr(classroom, "teacher_id"):
            return False

        if classroom.teacher_id == request.user.id:
            return True

        return Enrollment.objects.filter(
            user=request.user,
            classroom=classroom
        ).exists()
