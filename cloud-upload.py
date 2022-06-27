from firebase import firebase
import RPi.GPIO as GPIO
import dht11
import time
url="https://temp-7bca8-default-rtdb.firebaseio.com/Weather"
firebase = firebase.FirebaseApplication(url)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
instance = dht11.DHT11(pin=2)

while True:
  result = instance.read()
  if result.is_valid():
    print(“Temp: %d ” % result.temperature + ‘ ‘ +”Humid:%d %%”% result.humidity)
    temp = firebase.put(“Weather”,”Temp”, result.temperature)
    humid = firebase.put(“Weather”, “Humid”, result.humidity)
  time.sleep(1)
