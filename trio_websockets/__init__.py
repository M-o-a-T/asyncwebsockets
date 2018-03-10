"""
Websocket library for curio + trio.
"""
from trio_websockets.client import connect_websocket
from trio_websockets.ws import ClientWebsocket, WebsocketBytesMessage, WebsocketClosed, \
    WebsocketConnectionEstablished, WebsocketConnectionFailed, WebsocketMessage, \
    WebsocketTextMessage

__all__ = ["connect_websocket", "ClientWebsocket",
           "WebsocketClosed", "WebsocketBytesMessage", "WebsocketTextMessage", "WebsocketMessage",
           "WebsocketConnectionEstablished", "WebsocketConnectionFailed"]
