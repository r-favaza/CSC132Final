import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lights = []
floor1 = 16; lights.append(floor1)
floor2 = 12; lights.append(floor2)
floor3 = 4; lights.append(floor3)
section1 = 18; lights.append(section1)
section2 = 22; lights.append(section2)

for i in lights:
    GPIO.setup(lights, GPIO.OUT)

def allOff():
    for i in lights:
        GPIO.output(i, False)

allOff()

while True:
    userInput = str(input("What lights do you want to turn on? "))

    if userInput == "None":
        allOff()

    if "f1" in userInput:
        GPIO.output(floor1, True)
        GPIO.output(floor2, False)
        GPIO.output(floor3, False)

    elif "f2" in userInput:
        GPIO.output(floor1, False)
        GPIO.output(floor2, True)
        GPIO.output(floor3, False)

    elif "f3" in userInput:
        GPIO.output(floor1, False)
        GPIO.output(floor2, False)
        GPIO.output(floor3, True)

    if "s1" in userInput:
        GPIO.output(section1, True)
        GPIO.output(section2, False)

    elif "s2" in userInput:
        GPIO.output(section1, False)
        GPIO.output(section2, True)