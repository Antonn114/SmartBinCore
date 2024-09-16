from socket import *
from struct import pack
from SBCamera import SBCamera

camera = SBCamera()

class ClientProtocol:

    def __init__(self):
        self.socket = None
        self.listen_socket = None

    def listen(self, server_inp, server_port):

    def connect(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((server_ip, server_port))
        print("Connection ok!")

    def close(self):
        self.socket.shutdown(SHUT_WR)
        self.socket.close()
        self.socket = None

    def send_image(self, image_data):

        # use struct to make sure we have a consistent endianness on the length
        length = pack('>Q', len(image_data))

        # sendall to make sure it blocks if there's back-pressure on the socket
        self.socket.sendall(length)
        self.socket.sendall(image_data)

        ack = self.socket.recv(1)

        # could handle a bad ack here, but we'll assume it's fine.

    def receive_ans(self):




if __name__ == '__main__':
    cp = ClientProtocol()


    while True:
        input()
        image_data = None

        camera.capture_one("data/captured.jpg")

        with open('./data/captured.jpg', 'rb') as fp:
            image_data = fp.read()

        assert(len(image_data))
        cp.connect('192.168.85.39', 55555)
        cp.send_image(image_data)
        cp.receive_ans()
        cp.close()

