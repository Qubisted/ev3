#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
motorb_l = Motor(Port.B)
motorc_r = Motor(Port.C)

# Starting jingle.
ev3.speaker.play_notes(['C4/4', 'D4/4', 'E4/4'], tempo=520)

# Initialize the drive base.
car = DriveBase(motorb_l, motorc_r, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for one meter.
car.straight(100)
ev3.speaker.beep()

car.straight(-100)
ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
car.turn(360)
ev3.speaker.beep()

car.turn(-360)
ev3.speaker.beep()

ev3.speaker.play_notes(['E4/4', 'D4/4', 'C4/4'], tempo=520)