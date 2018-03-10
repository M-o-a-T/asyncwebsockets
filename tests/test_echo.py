import pytest

from trio_websockets.client import connect_websocket
from trio_websockets.ws import WebsocketConnectionEstablished, WebsocketBytesMessage

@pytest.mark.trio
async def test_echo():
    sock = await connect_websocket("ws://echo.websocket.org", reconnecting=False)
    rcvd = 0
    async for message in sock:
        print("Event received", message)
        if isinstance(message, WebsocketConnectionEstablished):
            await sock.send_message(b"test")

        elif isinstance(message, WebsocketBytesMessage):
            assert message.data == b"test"
            rcvd += 1
            await sock.aclose(code=1000, reason="Thank you!")

    assert rcvd == 1

@pytest.mark.trio
async def test_secure_echo():
    sock = await connect_websocket("wss://echo.websocket.org", reconnecting=False)
    rcvd = 0
    async for message in sock:
        print("Event received", message)
        if isinstance(message, WebsocketConnectionEstablished):
            await sock.send_message(b"test")

        elif isinstance(message, WebsocketBytesMessage):
            assert message.data == b"test"
            rcvd += 1
            await sock.aclose(code=1000, reason="Thank you!")
    assert rcvd == 1

