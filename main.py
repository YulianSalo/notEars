#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

LEDBlue = 18
        
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, GPIO.LOW)

LEDGreen = 22
        
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, GPIO.LOW)

LEDRed = 27
        
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, GPIO.LOW)


def callback(channel):
        if GPIO.input(channel):
                print "Sound Detected!"

                GPIO.output(LEDGreen, GPIO.HIGH)  #Turn on LED
        
                time.sleep(0.5)    

                GPIO.output(LEDGreen, GPIO.LOW)   #Turn off LED
        else:
                print "Sound Detected!"

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)

        GPIO.output(LEDBlue, GPIO.HIGH)  #Turn on LED

    	time.sleep(2.5) 