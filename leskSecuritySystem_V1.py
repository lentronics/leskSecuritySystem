#Lesk Security System version 1.0.0
#Created by Lesk Corporation:
#	Pedro Bettoni & Pedro Resende Costa
#for more information about this project visit:
# https://github.com/pedrobettoni/leskSecuritySystem
# http://pedrobettoni.website/2016/07/29/raspberry-pi-motion-security-system






from subprocess import Popen, PIPE #To get the string time
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import sys

#Declaring and initialize 16x2 LCD object
lcd = Adafruit_CharLCD(pin_rs=26, pin_e=19, pins_db=[13, 6, 5, 11])
lcd.begin(16,1)

#Declare and initialize camera
from picamera import PiCamera
from time import sleep
camera = PiCamera()


#Set GPIO  pin numbering.
GPIO.setmode(GPIO.BCM)

#PIR sensor input pin
PIR_PIN = 9

# defining PIR_PIN as an input.
GPIO.setup(PIR_PIN, GPIO.IN)


#Starting the program
try:
       #Welcome messages that will be displayed on the lcd
        t = 'Lesk Corporation'
        t2 = 'Security System'
        t3 = 'Starting........'
	t4 = 'System is on....' 
        lcd.clear()

        for i in t:
                lcd.message(i)
                time.sleep(0.03)

        lcd.message('\n ')
        for i2 in t2:
                lcd.message(i2)
                time.sleep(0.03)
        lcd.clear()

        for i3 in t3:
                lcd.message(i3)
                time.sleep(0.03)
        lcd.message('\n')

        for i4 in range(0, 16):
                lcd.message('.')
                time.sleep(0.03)

        lcd.clear()
		
        while True:
	
		if GPIO.input(PIR_PIN):
			lcd.clear()
			lcd.message('Hostile Detected\n')
			stdout = Popen('date +%Y%m%d%H%M%S', shell=True, stdout=PIPE).stdout
  		        time23 = stdout.read()

			#Camera start recording and will save the video in the following path, feel free to change acccording to your system
			camera.start_recording('/home/pi/Documents/motionSensor/records/%s.h264' % time23)
			lcd.message('Recording Video...')
			sleep(5) #Change the number for time recording
			lcd.clear()
			camera.stop_recording() #Stop recording video
                        lcd.message('Video Recorded\n') #Video was successfully recorded and saved 
			sleep(2)
			lcd.clear()
			for i in t4:
				lcd.message(i)
				time.sleep(0.1)
			lcd.message('\n')
			for i in range(0,16):
				lcd.message('.')		
				sleep(0.1)	

			


except KeyboardInterrupt:
	lcd.clear()
        lcd.message('System is OFF')
        GPIO.cleanup()

