from django.db import models
import uuid
from classrooms.models import Classroom
from accounts.models import User


class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="materials"
    )
    title = models.CharField(max_length=255)
    youtube_url = models.URLField
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.classroom.title}"


class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="submissions"
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submissions"
    )
    file = models.FileField(upload_to="submissions/%Y/%m/%d/")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    graded = models.BooleanField(default=False)
    grade = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
