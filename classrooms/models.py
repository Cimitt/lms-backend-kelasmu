from django.db import models
import uuid
import secrets
import string
from accounts.models import User


def generate_class_token(lenght=6):
    letters = string.ascii_uppercase
    return "".join(secrets.choice(letters) for _ in range(lenght))


class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="classrooms"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    join_token = models.CharField(
        max_length=6, unique=True, default=generate_class_token
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def regenerate_token(self):
        self.join_token = generate_class_token()
        self.save()

    def __str__(self):
        return f"{self.title} ({self.teacher})"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="enrollments"
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "classroom")
