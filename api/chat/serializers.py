from rest_framework import serializers
from chat.models import ClassChatMessage, DirectChatMessage, ChatAttachment
from api.auth.serializerss import UserSerializer
from api.materials.serializers import MaterialSerializer


class ClassChatMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = ClassChatMessage
        fields = ["id", "material", "sender", "content", "timestamp"]


class DirectChatMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = DirectChatMessage
        fields = ["id", "sender", "recipient", "content", "timestamp"]


class ChatAttachmentSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)

    class Meta:
        model = ChatAttachment
        fields = ["id", "file", "uploaded_by", "created_at"]
