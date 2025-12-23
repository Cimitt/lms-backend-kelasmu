from django.db import models
from materials.models import Material
from accounts.models import User


class ClassChatMessage(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="chat_message"
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    mesasge = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class DirectChatMessage(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_direct_messages"
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_direct_messages",
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ChatAttachment(models.Model):
    file = models.FileField(upload_to="chat_attachments/")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uploaded_by} - {self.file.name}"


# Create your models here.
