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
 
def tapp(): # a long tap i hope
  pwm.setPWM(2, 0, 200)
  time.sleep(2)
  pwm.setPWM(2, 0, 500)

while "True":
  y = raw_input("Which servo?")
  if y == "2":
    tap()
  elif y == "0":
    tapp()
  else:
    if y == "6":
      x = raw_input("Where?")
      pwm.setPWM(int(y), 0, int(x))
      record[int(y)] = int(x) 
      print "....", record[1], record[6]
    else:
      x = raw_input("Where?")
      if x > 280:
        pwm.setPWM(int(y), 0, int(x))
        record[int(y)] = int(x) 
        print "....", record[1], record[6]

