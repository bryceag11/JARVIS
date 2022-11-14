import asyncio
import websockets
import netifaces as ni
import time

nucIP = ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
print("NUC IP is: " + nucIP)

# create handler for each connection
data = ""

async def handler(websocket, path):
    while(True):
        data = await websocket.recv()
        reply = f"Data recieved as:  {data}"
        print(reply)
        await websocket.send(reply)
 
start_server = websockets.serve(handler, nucIP, 8000)

while(True): 
    try:
        asyncio.get_event_loop().run_until_complete(start_server)
    except:
        time.sleep(1)
asyncio.get_event_loop().run_forever()