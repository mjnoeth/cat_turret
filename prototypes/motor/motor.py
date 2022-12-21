#!/usr/bin/env python3

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()

for i in range(1000):
  kit.stepper1.onestep(direction=stepper.BACKWARD)

for i in range(1000):
  kit.stepper1.onestep()

