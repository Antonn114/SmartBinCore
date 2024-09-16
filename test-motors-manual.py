#!/usr/bin/python3

import signal

from DRV8825 import DRV8825
from time import sleep
import sys

motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

motor1.SetMicroStep('softward' ,'fullstep')
motor2.SetMicroStep('softward' ,'fullstep')

delay = 0.0002
def stop_motors(sig, frame):
    print("Stopped")
    motor1.Stop()
    motor2.Stop()
    sys.exit(0)

# 1 b 1700 -  1 f 1700
# 4500, 1400, 1800, 4800

signal.signal(signal.SIGINT, stop_motors)
while True:
    usrinp = input().lower().split(' ')
    if (len(usrinp) < 3):
        pass
    if (usrinp[0] == '1'):
        if (usrinp[1] == 'b'):
            motor1.TurnStep(Dir='backward', steps=int(usrinp[2]), stepdelay=delay)
        elif (usrinp[1] == 'f'):
            motor1.TurnStep(Dir='forward', steps=int(usrinp[2]), stepdelay=delay)
        sleep(0.5)
        motor1.Stop()
    elif (usrinp[0] == '2'):
        motor1.TurnStep(Dir="forward", steps=0)
        if (usrinp[1] == 'b'):
            motor2.TurnStep(Dir='backward', steps=int(usrinp[2]), stepdelay=delay)
        elif (usrinp[1] == 'f'):
            motor2.TurnStep(Dir='forward', steps=int(usrinp[2]), stepdelay=delay)
        sleep(0.5)
        motor1.Stop()
        motor2.Stop()
