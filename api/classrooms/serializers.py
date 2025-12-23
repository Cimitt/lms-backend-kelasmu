from rest_framework import serializers
from classrooms.models import Classroom, Enrollment
from api.auth.serializerss import UserSerializer  # import serializer User


class ClassroomSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Classroom
        fields = ["id", "teacher", "title", "description", "join_token", "created_at"]


class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ["id", "user", "classroom", "joined_at"]
