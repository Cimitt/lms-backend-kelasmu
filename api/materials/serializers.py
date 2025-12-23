from rest_framework import serializers
from materials.models import Material, Submission
from api.classrooms.serializers import (
    ClassroomSerializer,
)  # import serializer Classroom
from api.auth.serializerss import UserSerializer


class MaterialSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(read_only=True)

    class Meta:
        model = Material
        fields = [
            "id",
            "classroom",
            "title",
            "youtube_url",
            "description",
            "created_at",
        ]


class SubmissionSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = [
            "id",
            "material",
            "student",
            "file",
            "message",
            "created_at",
            "graded",
            "grade",
        ]
