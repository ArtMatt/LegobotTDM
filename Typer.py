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

file = open('codes.txt', 'r')

array = []
arrays1 = 0
arrays2 = 0
arrays3 = 0
z = 0
number = 0
x = file.read()
servovalue = 0

def typer():
  global z
  global number
  global servovalue
  for line in x:
    if line != " ":
      array.insert(z, line)
      z = z + 1
    else:
      arrays1 = array[-1]
      arrays2 = array[-2]
      arrays3 = array[-3]
      number = arrays3 + arrays2 + arrays1
      print number
      servovalue = int(number)
      commune()


def commune():
  time.sleep(1)
  pwm.setPWM(6, 0 , servovalue)

typer()
