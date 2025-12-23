from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from classrooms.models import Classroom, Enrollment
from api.classrooms.serializers import ClassroomSerializer, EnrollmentSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set teacher otomatis dari user login
        serializer.save(teacher=self.request.user)


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
