# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#originally named publisher_member_function.py

import asyncio
import websockets
import netifaces as ni
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import String   


class ServerPublisher(Node):

    def __init__(self):
        super().__init__('server_publisher')
        self.publisher_ = self.create_publisher(String, 'controls', 10)
        #timer_period = 0.5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        self.data = ""
        self.start = self.start_server()
        
    #def timer_callback(self):
    #    msg = String()
    #    msg.data = self.data #get from the socket connection later
    #    self.publisher_.publish(msg)
    #    self.get_logger().info('Publishing: "%s"' % msg.data)
        
    def start_server(self):

        nucIP = ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
        print("NUC IP is: " + nucIP)
    
        start_server = websockets.serve(self.handler, nucIP, 8000)

        while(True): 
            try:
                asyncio.get_event_loop().run_until_complete(start_server)
            except:
                time.sleep(1)
        asyncio.get_event_loop().run_forever()

    async def handler(self, websocket, path):
        while(True):
            #self.data = await websocket.recv()
            #self.publisher_.publish(self.data)
            msg = String()
            msg.data = await websocket.recv()
            self.publisher_.publish(msg)
            reply = f"Data recieved as:  {msg.data}"
            print(reply)
            await websocket.send(reply)

def main(args=None):

    rclpy.init(args=args)

    minimal_publisher = ServerPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
