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

while True:
    gui.Ui_Dialog.update()
    #if pyqt6.currentIndex() == 1:
     #   for j in range(21):
      #      GPIO.output(LEDs[j], 1)

    
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