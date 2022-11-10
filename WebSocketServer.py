import asyncio
 
import websockets

import socket
IPAddr=socket.gethostbyname(socket.getfqdn())
print(IPAddr)

# create handler for each connection
data = ""

async def handler(websocket, path):
    while(True):
        data = await websocket.recv()
        reply = f"Data recieved as:  {data}"
        print(reply)
        await websocket.send(reply)
 
start_server = websockets.serve(handler, IPAddr, 8000)
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()