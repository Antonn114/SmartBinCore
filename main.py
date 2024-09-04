#!/usr/bin/python3

from SBCamera import SBCamera
from SBVT import SBVT
from SBMotor import SBStepperMotor
from time import sleep
import cv2

# Initialize our components
camera = SBCamera()

# Model relative paths
# models/ee8225-group4-vit-trashnet-enhanced/
# models/garbage-classification/

vit = SBVT('models/ee8225-group4-vit-trashnet-enhanced/', 'models/ee8225-group4-vit-trashnet-enhanced/')
motor1 = SBStepperMotor(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
motor2 = SBStepperMotor(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

motor1.go_CCW(2000)
sleep(2)
motor1.go_CW(2000)


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
    print(res)
    # motor1.go_and_return(ans_step[ans_set.index(res)], motor2.go_and_return(2000, sleep(1.5)))
    if (res not in ans_set):
        res = 'other'
    motor1.go_and_return(ans_step[ans_set.index(res)], sleep(1.5))

    # The function above does the following:

    # turn motor1 to the answer's respective position
    # turn motor2 to 112.5 degrees
    # wait for 1.5 seconds
    # turn motor2 back to original position
    # turn motor1 back to original position

'''