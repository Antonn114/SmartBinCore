#!/usr/bin/python

from SBCamera import SBCamera
import cv2
import tflite_runtime.interpreter as tflite


camera = SBCamera()
camera.capture_one('data/captured.jpg')
image = cv2.imread('data/captured.jpg')

