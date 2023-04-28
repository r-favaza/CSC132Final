import gui
import RPi.GPIO as GPIO
import pyqt6

#GPIO SETUP
GPIO.setmode(GPIO.BCM)

LEDs = []
for i in range(1, 23):
    LEDs.append(GPIO.setup(i, GPIO.OUT)) 

lights = []

floor1 = 4; lights.append(floor1)
floor2 = 12; lights.append(floor2)
floor3 = 16; lights.append(floor3)
section1 = 18; lights.append(section1)
section2 = 22; lights.append(section2)

for i in lights:
    GPIO.setup(lights, GPIO.OUT)

#GPIO.setup(17, GPIO.OUT) #set LED to pin 17

def allOff():
    for i in lights:
        GPIO.output(lights, False)

if gui.ui.listTabWidget.currentIndex() == 2:
    
    if gui.ui.tabWidget_5.currentIndex() == 0:
        allOff()
        GPIO.output(floor1, True)

        if gui.ui.tabWidget_6.currentIndex() == 0:
            GPIO.output(section1, True)

        elif gui.ui.tabWidget_6.currentIndex() == 1:
            GPIO.output(section2, True)

    elif gui.ui.tabWidget_5.currentIndex() == 1:
        allOff()
        GPIO.output(floor2, True)

        if gui.ui.tabWidget_7.currentIndex() == 0:
            GPIO.output(section1, True)

        elif gui.ui.tabWidget_7.currentIndex() == 1:
            GPIO.output(section2, True)

    elif gui.ui.tabWidget_5.currentIndex() == 2:
        allOff()
        GPIO.output(floor3, True)

        if gui.ui.tabWidget_8.currentIndex() == 0:
            GPIO.output(section1, True)

        elif gui.ui.tabWidget_8.currentIndex() == 1:
            GPIO.output(section2, True)

else:
    allOff()