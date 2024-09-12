#!/usr/bin/python3

from SBCamera import SBCamera
import cv2
from SBVT import SBVT

vit = SBVT('models/ee8225-group4-vit-trashnet-enhanced/', 'models/ee8225-group4-vit-trashnet-enhanced/')

camera = SBCamera()
camera.capture_one('data/captured.jpg')
image = cv2.imread('data/captured.jpg')
dst = cv2.fastNlMeansDenoisingColored(image,None,3,3,7,21)
print(image.shape)
crop_img = image[616:616+1232, 820:820+1640]
cv2.imwrite('data/out.jpg', crop_img)
res = vit.predict_image(crop_img)
print(res)