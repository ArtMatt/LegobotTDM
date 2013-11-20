#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM

import time
import shortcombo
import master

pwm = PWM(0x40, debug=True)


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  master.zip(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

file = open('codes.txt', 'r')

x = file.read()
currentvalue = 0
nice = 0

def typer():
  master.renew()
  global currentvalue
  global number
  global servovalue
  for line in x:
    if line != " ":
      currentvalue = line
      servovalue = shortcombo.key(currentvalue)
      commune(servovalue)
      master.taps()            
      master.renew() 
    elif line == "\n":
      print '... NOW WHAT!?'
    else:
      master.bl()
      time.sleep(.4) 
      master.taps()            
      master.renew() 
      print "...Entered"
      time.sleep(3)

def commune(coords):
  if coords[-1] == 3:
    master.br()
    master.taps()
    master.renew() 
    time.sleep(.4) 
    print int(coords[0])
    nice = int(coords[0])
    master.zip(1, nice)
    time.sleep(.4) 
    master.zip(6, coords[1])
    time.sleep(.4) 
    master.taps()
    master.renew() 
    time.sleep(.4)
    master.br()
  elif coords[-1] == 2:
    time.sleep(.1)
    master.zip(1, 330)
    time.sleep(.1)
    master.zip(6, 520)
    master.taps()
    master.renew() 
    time.sleep(.4) 
    master.zip(1, int(coords[0]))
    time.sleep(.4) 
    master.zip(6, int(coords[1]))
    time.sleep(.4) 
  else:
    time.sleep(.4) 
    master.zip(1, int(coords[0]))
    time.sleep(.4) 
    master.zip(6, int(coords[1]))
    time.sleep(.4) 

def gotoarmy():
  master.zip(1, 300)
  master.zip(6, 250)
  master.taps()
  time.sleep(5)
  master.zip(1, 500)
  master.zip(6, 200)
  master.taps()
  time.sleep(5)
  master.zip(1, 415)
  master.zip(6, 200)
  master.taps()
  time.sleep(5)
  master.zip(1, 375)
  master.zip(6, 400)
  master.taps()

gotoarmy()
typer()
