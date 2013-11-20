#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import shortcombo
import tap

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

file = open('codes.txt', 'r')

x = file.read()
currentvalue = 0
#servovalue = 0

def typer():
  global currentvalue
  global number
  global servovalue
  for line in x:
    if line != "\n":
      currentvalue = line
      print line
      print "did this work?"
      servovalue = shortcombo.key(currentvalue)
      print servovalue
     # commune()


def commune():
  time.sleep(1)
  pwm.setPWM(6, 0 , servovalue)

typer()
