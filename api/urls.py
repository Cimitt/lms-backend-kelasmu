from rest_framework.routers import DefaultRouter

# import viewsets dari masing-masing app
from api.auth.views import AuthViewSet  # misal login/logout/register
from api.classrooms.views import ClassroomViewSet, EnrollmentViewSet
from api.materials.views import MaterialViewSet, SubmissionViewSet
from api.chat.views import (
    ClassChatMessageViewSet,
    DirectChatMessageViewSet,
    ChatAttachmentViewSet,
)

router = DefaultRouter()

# Auth
router.register(r"auth", AuthViewSet, basename="auth")

# Classrooms
router.register(r"classrooms", ClassroomViewSet, basename="classrooms")
router.register(r"enrollments", EnrollmentViewSet, basename="enrollments")

# Materials
router.register(r"materials", MaterialViewSet, basename="materials")
router.register(r"submissions", SubmissionViewSet, basename="submissions")

# Chat
router.register(r"class-chat", ClassChatMessageViewSet, basename="class-chat")
router.register(r"direct-chat", DirectChatMessageViewSet, basename="direct-chat")
router.register(r"chat-attachments", ChatAttachmentViewSet, basename="chat-attachments")

urlpatterns = router.urls
