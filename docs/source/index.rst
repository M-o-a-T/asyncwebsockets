.. trio-websockets documentation master file, created by
   sphinx-quickstart on Wed Jan 24 23:59:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to trio-asyncio's documentation!
===========================================

trio-asyncio is a Python 3.6+ library for interacting with websockets over the internet from
asynchronous code. Trio-asyncio is designed around `trio`_, allowing it to work with
multiple async backends without any modifications.

It is a fork of `asyncwebsockets`_, dispensing with multio / curio
compatibility and using a trio-ish name.

.. asyncwebsockets: https://github.com/Fuyukai/asyncwebsockets

Installation
============

To install the latest stable version::

    $ pip install trio_websockets

To install the latest development version::

    $ pip install git+https://github.com/M-o-a-T/trio-websockets.git#egg=trio_websockets


Basic Usage
===========

To open a new websocket connection to a server, use :func:`.connect_websocket`:

.. autofunction:: trio_websockets.client.connect_websocket
    :async:

This will return a new :class:`.ClientWebsocket`, which is the main object used for communication
with the server.

You can get new events from the websocket by async iteration over the websocket object, like so:

.. code-block:: python3

    async for evt in websocket:
        print(type(evt))  # handle event appropriately

You can send data to the websocket in response with :meth:`.ClientWebsocket.send_message`:

.. code-block:: python3

    async for evt in websocket:
        if isinstance(evt, WebsocketBytesMessage):
            await websocket.send_message(b"Thanks for the message!")

.. automethod:: trio_websockets.ws.ClientWebsocket.send_message
    :async:

Finally, the websocket can be closed with the usage of :meth:`.ClientWebsocket.close`:

.. code-block:: python3

    await websocket.close(1000, reason="Goodbye!")

.. automethod:: trio_websockets.ws.ClientWebsocket.close

Event Listing
=============

A full listing of events that can be yielded from the websockets can be found here.

.. py:currentmodule:: trio_websockets.ws

.. autoclass:: WebsocketMessage
.. autoclass:: WebsocketTextMessage
.. autoclass:: WebsocketBytesMessage
.. autoclass:: WebsocketClosed
.. autoclass:: WebsocketConnectionEstablished
.. autoclass:: WebsocketConnectionFailed

Changelog
=========

0.2.0
-----

 - Redesign API significantly.

0.1.0
-----

 - Initial release.


.. trio: https://github.com/python-trio/trio
