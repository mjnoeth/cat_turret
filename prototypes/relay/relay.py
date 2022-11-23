#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
from getkey import getkey, keys

RelayPin = 11    # pin11

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(RelayPin, GPIO.OUT)
  GPIO.output(RelayPin, GPIO.LOW)

def loop():
  while True:
    print("press f to fire")
    key = getkey()
    if key == 'f':
      GPIO.output(RelayPin, GPIO.HIGH)
      print('high')
      time.sleep(.5)
      GPIO.output(RelayPin, GPIO.LOW)
      print('low')

def destroy():
  GPIO.output(RelayPin, GPIO.LOW)
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    print("ready")
    loop()
  except KeyboardInterrupt:
    destroy()


