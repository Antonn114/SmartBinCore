#!/usr/bin/python3

from DRV8825 import DRV8825
from time import sleep

motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

motor1.SetMicroStep('softward' ,'fullstep')
motor2.SetMicroStep('softward' ,'fullstep')

speed = 3250
delay = 0.0002

motor1.TurnStep(Dir='forward', steps=speed, stepdelay=delay)
sleep(0.5)
motor2.TurnStep(Dir='forward', steps=4000, stepdelay=delay)
sleep(0.5)
motor2.TurnStep(Dir='backward', steps=4000, stepdelay=delay)
sleep(0.5)
motor2.Stop()
sleep(0.5)
motor1.TurnStep(Dir='backward', steps=speed, stepdelay=delay)
sleep(0.5)
motor1.Stop()
