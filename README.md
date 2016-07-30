#Lesk Security System version 1.0.0
#Created by Lesk Corporation:
#       Pedro Bettoni & Pedro Resende Costa
#for more information about this project visit:
# https://github.com/pedrobettoni/leskSecuritySystem
# http://pedrobettoni.website/2016/07/29/raspberry-pi-motion-security-system

# leskSecuritySystem
Create a security system using a Raspberry Pi board, Raspberry Pi camera, 16x2 LCD and a PIR sensor. The PIR sensor will activate the camera when motion is detected and record a short video everytime motion is detected. The video is then saved to the raspberry pi storage system.

Make sure to install the Adafruit Python library:
sudo apt-get update
sudo apt-get install -y python3 python3-pip python-dev
sudo pip3 install rpi.gpio
For more information, visit Adafruit github page: https://github.com/adafruit/Adafruit_Python_CharLCD

Upcomming work:
1. Use a Python script to upload the recorded video to our web domain
2. Web application to:
   . provide access to uploaded videos
   . delivery an e-mail notification of motion detect events with link to the uploaded video
   . data visualization with statistics of recent activities
