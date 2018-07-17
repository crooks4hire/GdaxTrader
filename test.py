# gdax/WebsocketClient.py
# original author: Daniel Paquin
# mongo "support" added by Drew Rice
#
#
# Template object to receive messages from the gdax Websocket Feed
# Test edit from github!

from __future__ import print_function
import sys
from colorama import init, Fore, Back, Style
import gdax
import json
import base64
import hmac
import hashlib
import time
from threading import Thread
from websocket import create_connection, WebSocketConnectionClosedException

init()

class MyWebsocketClient(gdax.WebsocketClient):
		def on_open(self):
			self.url = "wss://ws-feed.gdax.com/"
			self.products = ["LTC-USD"]
			self.message_count = 0
			print("Let's count the messages!")

		def on_message(self, msg):
			if msg["type"]=="match":
				#print(json.dumps(msg, indent=4, sort_keys=True))
				price = msg["price"]
				side = msg["side"]
				
				if side == "sell":
					print(Back.GREEN, end="")
				else:
					print(Back.RED, end="")
				print(side + "\t", end=" ")
				print(price[:5], end="")
				print(Style.RESET_ALL)
			self.message_count += 1

		def on_close(self):
			print("-- Goodbye! --")

wsClient = MyWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products)

try: 
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	wsClient.close()
