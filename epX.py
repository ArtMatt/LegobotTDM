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

def tap():
  pwm.setPWM(2, 0, 200)
  time.sleep(.5)
  pwm.setPWM(2, 0, 500)

def type():
  y = raw_input("... Servo 1? >> ")
  if y == "t":
    tap()
    type()
  else:
    go()

def go():
  pwm.setPWM(1, 0, int(y))
  x = raw_input("....Servo 6? >> ")
  pwm.setPWM(6, 0, int(x))
  time.sleep(.1)
  tap()
  record[1] = y
  record[6] = x
  print "....", record[1], record[6]

while "True":
  type()
