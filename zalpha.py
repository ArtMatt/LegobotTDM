#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address.
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMinn = 1  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoMid = 375
servoMaxx = 740
servoMaxxx = 760 
y = "yes"
m = 375


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

while y != "no":
  # oldcomment Change speed of continuous servo on channel O
  pwm.setPWM(1, 0, int(m))
  print ">>>> M value is: ", m
  m = raw_input("Now what? >> ")
  if m != "stop" and int(m) > 149 and int(m) < 601:
    pwm.setPWM(1, 0, int(m))
  elif int(m) < 150:
    m = 150
    pwm.setPWM(1, 0, int(m))
  elif int(m) > 600:
    m = 600
    pwm.setPWM(1, 0, int(m)) 
  else:
    y = "no"
    print "murder she wrote"   

# END OF FILE

