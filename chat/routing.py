from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path 
from . import consumers

websocket_urlpatterns = [
    #re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
    re_path(r'^ws/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]

# the websocket will open at 127.0.0.1:8000/ws/<room_name>
application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
    ,
})