#!/usr/bin/python           # This is client.py file

from socket import *
from struct import pack
from SBCamera import SBCamera
import cv2
import numpy as np

camera = SBCamera()
s = socket()

def send_image(image_data):
    length = pack('>Q', len(image_data))

    s.sendall(length)
    s.sendall(image_data)

    ack = s.recv(1)

def rec_ans():
    ans = s.recv(1024)
    print(ans.decode())
    s.sendall(b'\00')
    


host = "192.168.85.39" # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
while True:
    inp_img = input()
    image_data = None

    # camera.capture_one("data/captured.jpg")
    
    with open(inp_img, 'rb') as fp:
        image_data = fp.read()

    assert(len(image_data))
    send_image(image_data)
    rec_ans()


s.close()
