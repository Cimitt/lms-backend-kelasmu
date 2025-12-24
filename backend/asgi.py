import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# set environment variable for django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# get the django ASGI app
django_asgi_app = get_asgi_application()

# import routing after django is ready
import api.chat.routing

# define asgi app routing
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # handle HTTP requests via django
    "websocket": AuthMiddlewareStack(  # handle ws connections
        URLRouter(
            api.chat.routing.websocket_urlpatterns  # your ws routing
        )
    ),
})
