import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request_counter = 0
send_message = input("Enter item: ")


request_counter += 1
print("Sending request %s …" % request_counter)
socket.send(send_message.encode())

#  Get the reply.
message = socket.recv()
message = message.decode()
print("Received reply: %s" % message)
