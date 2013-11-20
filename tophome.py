#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoMid = 372  
x = 0
y = 0
record = [0, 0, 0, 0, 0, 0, 0]

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

def slide():
  pwm.setPWM(2, 0, 500)
  pwm.setPWM(1, 0, 600)
  time.sleep(.7)
  pwm.setPWM(6, 0, 305)
  time.sleep(.5)
  pwm.setPWM(2, 0, 200)
  time.sleep(.2)
  pwm.setPWM(1, 0, 500)
  time.sleep(.5)
  pwm.setPWM(2, 0, 500)

slide()
