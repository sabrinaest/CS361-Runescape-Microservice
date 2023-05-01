import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request_counter = 0

while True:
    request_counter += 1
    print("Sending request %s …" % request_counter)
    send_message = input("Enter item (or 1 to quit): ")

    if send_message == '1':
        break

    socket.send(send_message.encode())

    #  Get the reply.
    reply_data = socket.recv()
    reply_data = reply_data.decode()
    data = json.loads(reply_data)

    if 'error_message' in data:
        print('ERROR: ' + data['error_message'])

    else:
        item_name = data['item_name']
        price = data['price']
        wiki_link = data['wiki_page']
        print("Item name: " + item_name + "     price: " + str(price) + "coins" + "     wiki page: " + wiki_link)
