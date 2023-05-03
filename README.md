# CS361-Runescape-Microservice

# [Runescape Microservice UML Diagram](https://user-images.githubusercontent.com/102570901/236058526-bc69d675-faae-439a-9ce1-d34b9add1a7a.jpg)

#The microservice will use ZeroMQ (PyZMQ Messaging) for communication.

# How to REQUEST data (example call included): The client will send a socket with the item name stored as a string. 
# Example:
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(“tcp://localhost:5555”)

request_item = “Shoulder_parrot”
socket.send(request_item.encode())

# How to RECEIVE data: The microservice service will listen to the requests being sent to ZeroMQ, it will then process the item name string. 
# It will then send a GET request to the Old School Runescape API and processed the received data. 

#Clear instructions for how to RECEIVE data from the microservice you implemented
#UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand
