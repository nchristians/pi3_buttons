#to be run on raspberry pi 3
#import libraries
from picamera import PiCamera
import RPi.GPIO as GPIO
import datetime
from time import sleep

#setup IO
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#setup camera
camera = PiCamera()
camera.resolution = (640, 480)

print("Here we go! Press CTRL+C to exit")

try:
        GPIO.wait_for_edge(15, GPIO.FALLING)
        print("Button was pressed!")
        camera.start_preview()
        sleep(2)
        #file naming
        currentTime = datetime.datetime.now()
        timestamp = currentTime.strftime("%d-%m-%y_%H-%M-%S")
        imageName = "%s.jpg" % timestamp
        
        #save picture
        camera.capture("%s" %imageName)
        print("File name is %s" %imageName)
        GPIO.cleanup()

#this doesn't actually break out for some reason
#this doesn't actually break out for some reason
except KeyboardInterrupt:
        GPIO.cleanup()
