# CS361-Runescape-Microservice

# The microservice will use ZeroMQ (PyZMQ Messaging) for communication.

# How to REQUEST data (example call included): The client will send a socket with the item name stored as a string. 
# Example:
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(“tcp://localhost:5555”)

request_item = “Shoulder_parrot”
socket.send(request_item.encode())

# How to RECEIVE data: The microsevice will send the processed data (from API) back to the client through ZeroMQ. The client must import json and use json.loads() to 
# convert it to a python dictionary. The dictionary will have the item_name, price, wiki page or error as dictionary keys. 
# Include a statement to check if the microservice could not retrieve the item information.
# Example: 
reply_data = socket.recv()
reply_data = reply_data.decode()
data = json.loads(reply_data)

if 'error_message' in data:
  print('ERROR: ' + data['error_message'])

else:
  item_name = data['item_name']
  price = data['price']
  wiki_link = data['wiki_page']
  print("Item name: " + item_name + "     price: " + str(price) + " coins" + "     wiki page: " + wiki_link)

# [Runescape Microservice UML Diagram](https://user-images.githubusercontent.com/102570901/236058526-bc69d675-faae-439a-9ce1-d34b9add1a7a.jpg)

