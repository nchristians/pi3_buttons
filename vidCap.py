#to be run on raspberry pi 3
#import libraries
import picamera
import RPi.GPIO as GPIO
import datetime
import os

#setup gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#camera setup
camera = picamera.PiCamera()
camera.framerate = 25
camera.resolution = (640, 480)

print("Here we go! Press ctrl+c to stop.")

try:
        GPIO.wait_for_edge(14, GPIO.FALLING)
        print("Button was pressed! Recording!")

        #file naming
        currentTime = datetime.datetime.now()
        timestamp = currentTime.strftime("%d-%m-%y_%H-%M-%S")
        rawName = "%s.h264" %timestamp
        endName = "%s.mp4" %timestamp
        #recording
        camera.start_recording("%s" %rawName)
        print("Press button again to stop recording!")
        camera.wait_recording(2)
        GPIO.wait_for_edge(14, GPIO.FALLING)
        print("Recording stopped! File name is %s" %endName)

        #video conversion
        os.system("MP4Box -fps 25 -add %s %s" %(rawName, endName))
        camera.stop_recording

#doesn't actually break out for some reason
except  KeyboardInterrupt:
        GPIO.cleanup()

GPIO.cleanup()

#remove raw file
os.system("sudo rm -r %s" %rawName)
