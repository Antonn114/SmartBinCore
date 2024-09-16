from SBCamera import SBCamera
import cv2
from time import sleep

camera = SBCamera()

i = 0

def get_long_num(x: int):
    ret = ""
    largest_ten = 100000
    while(largest_ten >= 1):
        ret += str((x//largest_ten) % 10)
        largest_ten //= 10
    return ret



# set image
while True:
    input()
    camera.capture_one('data/set4/img' + get_long_num(i) + '.jpg')
    i += 1