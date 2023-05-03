import zmq
import requests
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    message = message.decode()
    print("Received request: %s" % message)

    response_API = requests.get('https://api.weirdgloop.org/exchange/history/osrs/latest?name=' + message + '&lang=en')
    data = response_API.text
    result = json.loads(data)

    if 'error' in result:
        if result['error'] == 'Item(s) not found in the database':
            error_reply = {'error_message': 'Item is not tradeable'}
            error_reply = json.dumps(error_reply)
            socket.send(bytes(error_reply, encoding="utf-8"))

    else:
        item_price = result[message]['price']

        wiki_lookup = message.replace(" ", '_')

        reply_back = {'item_name': message, 'price': item_price, 'wiki_page': 'https://oldschool.runescape.wiki/w/Exchange:' + wiki_lookup}
        json_data = json.dumps(reply_back)

        #  Send reply back to client
        socket.send(bytes(json_data,encoding="utf-8"))


