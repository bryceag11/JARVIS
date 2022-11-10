import asyncio
 
import websockets

import socket
IPAddr=socket.gethostbyname(socket.getfqdn())
print(IPAddr)

import netifaces as ni
ip = ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
print("My IP is: " + ip)

# create handler for each connection
data = ""

async def handler(websocket, path):
    while(True):
        data = await websocket.recv()
        reply = f"Data recieved as:  {data}"
        print(reply)
        await websocket.send(reply)
 
start_server = websockets.serve(handler, ip, 8000)
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()