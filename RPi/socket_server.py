#!/usr/bin/env python

import asyncio
import websockets
import os

async def echo(websocket, path):
    async for message in websocket:
        print("Received and echoing message: "+message, flush=True)
        await websocket.send(message)

start_server = websockets.serve(echo, "10.163.149.122", 8080)

print("WebSockets echo server starting", flush=True)
asyncio.get_event_loop().run_until_complete(start_server)

print("WebSocets echo server running", flush=True)
asyncio.get_event_loop().run_forever()
