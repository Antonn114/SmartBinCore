#!/usr/bin/python3

from SBCamera import SBCamera
import cv2
from SBVT import SBVT

vit = SBVT('models/garbage-classification/', 'models/garbage-classification/')

camera = SBCamera()
camera.capture_one('data/captured.jpg')
image = cv2.imread('data/captured.jpg')
print(image.shape)
res = vit.predict_image(image)
print(res)
