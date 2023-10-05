import websockets
import asyncio

data = ""
async def connectRpi():
    uri = "ws://10.163.149.122:8001"
    async with websockets.connect(uri) as websocket:
        await websocket.recv(data)
        print("data received {data}")