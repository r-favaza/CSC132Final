import gui
import RPi.GPIO as GPIO
import pyqt6

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
'''
LEDs Index
0 = 1st Floor
1 = 2nd floor
2 = 3rd floor
3 = 
4 = 
5 = 
6 = 
7 = 
8 = 
9 = 
10 = 
11 = 
13 = 
14 = 
15 = 
16 = 
17 = 
18 = 
19 = 
20 = 
21 = 
'''
LEDs = []
for i in range(1, 23):
    LEDs.append(GPIO.setup(i, GPIO.OUT)) 

<<<<<<< HEAD
while True:
    gui.Ui_Dialog.update()
    #if pyqt6.currentIndex() == 1:
     #   for j in range(21):
      #      GPIO.output(LEDs[j], 1)
=======
>>>>>>> c4ef95fe22fe0ef37e58b7dea09dac132cc5501f

<<<<<<< HEAD
=======
lights = []

floor1 = None; lights.append(floor1)
floor2 = None; lights.append(floor2)
floor3 = None; lights.append(floor3)
section1 = None; lights.append(section1)
section2 = None; lights.append(section2)

for i in lights:
    GPIO.setup(lights, GPIO.OUT)

#GPIO.setup(17, GPIO.OUT) #set LED to pin 17

def allOff():
    for i in lights:
        GPIO.output(lights, False)

if gui.ui.listTabWidget.currentIndex() == 2:
>>>>>>> c4ef95fe22fe0ef37e58b7dea09dac132cc5501f
    
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