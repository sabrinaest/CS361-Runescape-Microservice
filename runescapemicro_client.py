import zmq
import json
import multiprocessing

def send_request():
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

        if send_message == '1':     # used if the client wishes to exit
            break

        socket.send(send_message.encode())      # sends socket with item name to zero mq

        #  Get the reply.
        reply_data = socket.recv()
        reply_data = reply_data.decode()
        data = json.loads(reply_data)

        if 'error_message' in data:             # if there is an error message key something went wrong, so print the error message received.
            print('ERROR: ' + data['error_message'])

        else:
            item_name = data['item_name']       # else, print out the data that was sent back from zero mq
            price = data['price']
            wiki_link = data['wiki_page']
            print("Item name: " + item_name + "     price: " + str(price) + " coins" + "     wiki page: " + wiki_link)


if __name__ == '__main__':      # partner suggested adding this line of code to help with continuously running the microservice on their end, as they were running into issues with integration
    microservice_process = multiprocessing.Process(send_request())
    microservice_process.start()