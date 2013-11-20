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



def taps():
  time.sleep(.5)
  pwm.setPWM(2, 0, 500)
  time.sleep(.5)
  pwm.setPWM(2, 0, 200)
  time.sleep(.5)
  pwm.setPWM(2, 0, 500)
#!/usr/bin/python


def bl():
   time.sleep(.2)
   pwm.setPWM(1, 0, 300)
   time.sleep(.2)
   pwm.setPWM(6, 0, 170)
   time.sleep(.2)

def br():
   time.sleep(.2)
   pwm.setPWM(1, 0, 290)
   time.sleep(.2)
   pwm.setPWM(6, 0, 500)
   time.sleep(.2)

def renew():
  time.sleep(.2)
  pwm.setPWM(2, 0, 500)
  time.sleep(.2)
  pwm.setPWM(1, 0, 450)
  time.sleep(.2)
  pwm.setPWM(6, 0, 370)
  time.sleep(.2)

def zip(x, y):
  time.sleep(.2)
  pwm.setPWM(int(x), 0, int(y))  
  
