from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from chat.models import ClassChatMessage, DirectChatMessage, ChatAttachment
from api.chat.serializers import (
    ClassChatMessageSerializer,
    DirectChatMessageSerializer,
    ChatAttachmentSerializer,
)


class ClassChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ClassChatMessage.objects.all()
    serializer_class = ClassChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class DirectChatMessageViewSet(viewsets.ModelViewSet):
    queryset = DirectChatMessage.objects.all()
    serializer_class = DirectChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class ChatAttachmentViewSet(viewsets.ModelViewSet):
    queryset = ChatAttachment.objects.all()
    serializer_class = ChatAttachmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
