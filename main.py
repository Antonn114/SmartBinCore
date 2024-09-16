#!/usr/bin/python3

from SBCamera import SBCamera
from SBVT import SBVT
from DRV8825 import DRV8825
from time import sleep
import sys
import signal
import cv2

camera = SBCamera()
vit = SBVT('models/waste-classification/', 'models/waste-classification/')
motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

motor1.SetMicroStep('softward' ,'fullstep')
motor2.SetMicroStep('softward' ,'fullstep')

motor_delay = 0.00025

def stop_program(sig, frame):
    print("Stopped")
    motor1.Stop()
    motor2.Stop()
    sys.exit(0)

ans_idx = ["plastic", "metal", "glass", "other"]
motor_ans_speed_first = [4500, 1400, 1800, 4800]
motor_ans_speed_second = [4600, 1300, 1800, 4800]
motor_ans_dir_first = ['forward', 'forward', 'backward', 'backward']
motor_ans_dir_second = ['backward', 'backward', 'forward', 'forward']

signal.signal(signal.SIGINT, stop_program)
while True:
    input()
    camera.capture_one('data/captured.jpg')
    image = cv2.imread('data/captured.jpg')
    orig_h = image.shape[0]
    orig_w = image.shape[1]
    crop_img = image[orig_h//4:orig_h*3//4, orig_w//6: orig_w*4//6]
    cv2.imwrite('data/cropped.jpg', crop_img)
    res = vit.predict_image(crop_img)
    print(res)
    if (res not in ans_idx):
        res = "other"
    idx = ans_idx.index(res)
    motor1.TurnStep(Dir=motor_ans_dir_first[idx], steps=motor_ans_speed_first[idx], stepdelay=motor_delay)
    sleep(0.5)
    motor2.TurnStep(Dir="forward", steps=4000, stepdelay=motor_delay)
    sleep(1)
    motor2.TurnStep(Dir="backward", steps=4000, stepdelay=motor_delay)
    sleep(0.5)
    motor1.TurnStep(Dir=motor_ans_dir_second[idx], steps=motor_ans_speed_second[idx], stepdelay=motor_delay)
    sleep(0.5)
    motor1.Stop()
    motor2.Stop()
