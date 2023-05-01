import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    message = message.decode()
    print("Received request: %s" % message)

    result = getItemInfo(message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    message = result.encode()
    socket.send(message)


