import asyncio
import websockets
import time

rpiIP = "10.163.149.122"

#This will be run on startup
# 1. Opens up websocket server to listen for NUC IP being sent
# 2. Grabs IP from message
# 3. Edits/creates redirect HTML page (NUC remote interface IP) to serve on Apache server

nucIP = ""

async def handler(websocket, path):
    while(True):
        nucIP = await websocket.recv()
        reply = f"Data recieved as:  {nucIP}"
        print(reply)
        await websocket.send(reply)
 
start_server = websockets.serve(handler, rpiIP, 8001)

#while(True): 
#    try:
asyncio.get_event_loop().run_until_complete(start_server)
    #except:
        #time.sleep(1)
asyncio.get_event_loop().run_forever()

f = open("index.html", "w") 
f.write("<!DOCTYPE html>\n \
<html>\n \
    \t<head>\n \
        \t\t<title>ROBB redirect</title>\n \
     \t <meta charset=\"UTF-8\" />\n \
     \t <meta http-equiv=\"refresh\" content=\"0; URL=http://" + nucIP + " />\n \
   \t</head>\n \
   \t<body>\n \
     \t <p>If you have not been redirected within 1 second, the robot is probably offline.</p>\n \
   \t</body>\n \
</html>") 
f.close()