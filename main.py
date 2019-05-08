#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setwarnings(False) 

LEDBlue = 18
        
GPIO.setup(LEDBlue, GPIO.OUT)

GPIO.output(LEDBlue, GPIO.LOW)

LEDGreen = 22
        
GPIO.setup(LEDGreen, GPIO.OUT)

GPIO.output(LEDGreen, GPIO.LOW)

LEDRed = 27
        
GPIO.setup(LEDRed, GPIO.OUT)

GPIO.output(LEDRed, GPIO.LOW)

detectedSound = "Sound detected"

def callback(channel):
        if GPIO.input(channel):
                print (detectedSound)

                GPIO.output(LEDGreen, GPIO.HIGH)  #Turn on LED
        
                time.sleep(0.5)    

                GPIO.output(LEDGreen, GPIO.LOW)   #Turn off LED
        else:
                print (detectedSound)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)

        GPIO.output(LEDBlue, GPIO.HIGH)  #Turn on LED

    	time.sleep(2.5) 

    	GPIO.output(LEDBlue, GPIO.LOW)  #Turn off LED

    	#time.sleep(2.5) 
