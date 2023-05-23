import zmq
import requests
import json
import multiprocessing


def run_microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    while True:
        #  Wait for next request from client
        message = socket.recv()
        message = message.decode()
        print("Received request: %s" % message)     # print what the server received from client

        response_API = requests.get('https://api.weirdgloop.org/exchange/history/osrs/latest?name=' + message + '&lang=en')
        data = response_API.text
        result = json.loads(data)

        if 'error' in result:   # if there is an error key in the response, then the api could not find item
            if result['error'] == 'Item(s) not found in the database':
                error_reply = {'error_message': 'Item is not tradeable'}
                error_reply = json.dumps(error_reply)
                socket.send(bytes(error_reply, encoding="utf-8"))

        else:
            item_price = result[message]['price']   # get the price of item

            wiki_lookup = message.replace(" ", '_')     # used to create the link for the wiki article

            reply_back = {'item_name': message, 'price': item_price, 'wiki_page': 'https://oldschool.runescape.wiki/w/Exchange:' + wiki_lookup}
            json_data = json.dumps(reply_back)      # reply back to client with item name, price and wiki article link

            #  Send reply back to client
            socket.send(bytes(json_data,encoding="utf-8"))


if __name__ == '__main__':  # partner suggested adding this line of code to help with continuously running the microservice on their end, as they were running into issues with integration
    microservice_process = multiprocessing.Process(run_microservice())
    microservice_process.start()