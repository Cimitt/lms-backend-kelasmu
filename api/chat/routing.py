from django.urls import re_path
from api.chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/class-chat/(?P<material_id>\d+)/$', consumers.ClassChatConsumer.as_asgi()),
    re_path(r'ws/direct-chat/(?P<user_id>\d+)/$', consumers.DirectChatConsumer.as_asgi()),
]
