from django.urls import path

import websocket.routings
from websocket import consumers
from channels.routing import URLRouter
websocket_urlpatterns ={
    path("websocket/", URLRouter(websocket.routings.websocket_urlpatterns)),
}