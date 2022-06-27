import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True:
  GPIO.output(8, True)
  print("LED is on")
  time.sleep(1)
  GPIO.output(8, False)
  print("LED is off")
  time.sleep(2)
  
