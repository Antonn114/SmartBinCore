#!/usr/bin/python           # This is client.py file

from socket import *
from struct import pack
import cv2
import numpy as np

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

camera = Picamera2()
camera_config = camera.create_still_configuration(main={"size": (1000, 1000)}, lores={"size": (640, 480)}, display="lores")
camera.configure(camera_config)

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
    


host = "192.168.1.139" # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
camera.start_preview(Preview.NULL)
camera.start()

while True:
    input()
    image_data = None

    camera.capture_file("data/captured.jpg")
    
    with open("data/captured.jpg", 'rb') as fp:
        image_data = fp.read()

    assert(len(image_data))
    send_image(image_data)

    rec_ans()


s.close()
camera.stop()
camera.stop_preview()
