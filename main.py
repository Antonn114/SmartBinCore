#!/usr/bin/python3

from SBCamera import SBCamera
from SBVT import SBVT
from DRV8825 import DRV8825
from time import sleep
import cv2

# Initialize our components
camera = SBCamera()

# Model relative paths
# models/ee8225-group4-vit-trashnet-enhanced/
# models/garbage-classification/

vit = SBVT('models/ee8225-group4-vit-trashnet-enhanced/', 'models/ee8225-group4-vit-trashnet-enhanced/')
'''
motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
motor1.SetMicroStep('softward' ,'fullstep')
motor2.SetMicroStep('softward' ,'fullstep')

'''
ans_set = ['paper', 'metal', 'plastic', 'other']
ans_step = [0, 1600, 3200, 4800]

while True:
    inp = input()
    if (inp == 'q'):
        break
    camera.capture_one('data/captured.jpg')
    image = cv2.imread('data/captured.jpg')
    res = vit.predict_image(image)
    cv2.putText(image, res, 
    (300, 300), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    5,
    (255, 255, 255),
    5,
    2)
    cv2.imwrite('data/out.jpg', image)
    if (res not in ans_set):
        res = 'other'
    
    '''
    motor1.TurnStep(Dir='forward', steps=ans_step[ans_set.index(res)], stepdelay=0)
    sleep(0.5)
    motor2.TurnStep(Dir='forward', steps=2000, stepdelay=0)
    sleep(0.5)
    motor2.TurnStep(Dir='backward', steps=2000, stepdelay=0)
    sleep(0.5)
    motor1.TurnStep(Dir='backward', steps=ans_step[ans_set.index(res)], stepdelay=0)
    sleep(1.5)
    '''
