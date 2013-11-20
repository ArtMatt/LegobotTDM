#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time


pwm = PWM(0x40, debug=True)
t = "no"
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

def tap():
  pwm.setPWM(2, 0, 300)
  time.sleep(.2)
  pwm.setPWM(2, 0, 460)
  time.sleep(2)
  pwm.setPWM(2, 0, 300)

def check_range(r):
  if r < 150:
    r = 150
  elif r > 600:
    r = 600
  return r

def run():
  m = check_range(int(raw_input("  Where? >>")))
  pwm.setPWM(1, 0, m)
  t = raw_input("  Tap? >>")
  if t == "yes" or "y":
    tap()

pwm.setPWM(1, 0, 375)
time.sleep(.1)
pwm.setPWM(2, 0, 300)
print m

while (True):
  run()

