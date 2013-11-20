#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time


pwm = PWM(0x40, debug=True)


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

pwm.setPWM(2, 0, 500)
time.sleep(.1)
pwm.setPWM(1, 0, 475)
time.sleep(.1)
pwm.setPWM(6, 0, 300)

