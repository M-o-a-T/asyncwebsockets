import trio

from trio_websockets.client import connect_websocket
from trio_websockets.ws import WebsocketConnectionEstablished, WebsocketBytesMessage

async def test():
    sock = await connect_websocket("ws://echo.websocket.org", reconnecting=False)
    async for message in sock:
        print("Event received", message)
        if isinstance(message, WebsocketConnectionEstablished):
            await sock.send_message(b"test")

        elif isinstance(message, WebsocketBytesMessage):
            print("Got response:", message.data)
            await sock.aclose(code=1000, reason="Thank you!")

trio.run(test)

