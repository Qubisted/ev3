#!/usr/bin/env pybricks-micropython
#!/usr/bin/env python3
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from threading import Thread


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize the EV3 Brick and the IR Sensor
ev3 = EV3Brick()
obstacle_sensor = InfraredSensor(Port.S4)

# Initialize the motors.
motorb_l = Motor(Port.B)
motorc_r = Motor(Port.C)
data = DataLog('time', 'senspct')
watch = StopWatch()

# ev3.screen.set_font(big_font)
# ev3.screen.print(stats)

# Starting jingle.
ev3.speaker.play_notes(['C4/4', 'D4/4', 'E4/4'], tempo=520)

# Initialize the drive base.
car = DriveBase(motorb_l, motorc_r, wheel_diameter=55.5, axle_track=104)
big_font = Font(size=24, bold=True)
stats = obstacle_sensor.distance()

def theDrive():
    while True:
        # Begin driving forward at 200 millimeters per second.
        car.drive(200, 0)
        
        # Wait until an obstacle is detected. This is done by repeatedly
        # doing nothing (waiting for 10 milliseconds) while the measured
        # distance is still greater than 300 mm.
        while obstacle_sensor.distance() > 60:
            wait(10)
            
          
        # Drive backward for 300 millimeters.
        car.straight(-300)
        # Turn around by 120 degrees
        car.turn(120)   
        # Read sens and time
        senspct = wheel.obstacle_sensor.distance()
        time = watch.time()

        # Each time you use the log() method, a new line with data is added to
        # the file. You can add as many values as you like.
        # In this example, we save the current time and motor angle:
        data.log(time, senspct)

        # Wait some time so the motor can move a bit
        wait(100)
theDrive()

ev3.speaker.play_notes(['E4/4', 'D4/4', 'C4/4'], tempo=520)

