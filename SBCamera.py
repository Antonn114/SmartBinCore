#!/usr/bin/python3


from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

class SBCamera:
    def __init__(self):
        self.picam2 = Picamera2()
        self.encoder = H264Encoder(1000000)

    def capture_one(self, destination_file):
        self.picam2.start_preview(Preview.NULL)
        self.picam2.start_and_capture_file(destination_file)
        self.picam2.stop_preview()
