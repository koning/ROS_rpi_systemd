#!/usr/bin/env python  
# Simple script for shutting down the raspberry Pi at the press of a button.  
# by Inderpreet Singh  
#https://www.element14.com/community/docs/DOC-78055/l/adding-a-shutdown-button-to-the-raspberry-pi-b
  
import RPi.GPIO as GPIO  
import time  
import os  
 
# Pin to read for shutdown signal
SDGPIO=21
# Use the Broadcom SOC Pin numbers  
# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(SDGPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    os.system("sudo shutdown -h now")  
 
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(SDGPIO, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
 
# Now wait!  
while 1:  
    time.sleep(1)  
