import angleValues as angV
import RPi.GPIO as GPIO
import time

def setWrist(var, numberOfCycles):
    # Write the code for implementing gesture
    # Setup all Servos and then perform actions
    GPIO.setmode(GPIO. BOARD)
    # Finger 1
    GPIO.setup(11, GPIO.OUT)
    servo1 = GPIO.PWM(11, 50)
    servo1.start(0)

    # Finger 2
    GPIO.setup(11, GPIO.OUT)
    servo2 = GPIO.PWM(11, 50)
    servo2.start(0)

    # Finger 3
    GPIO.setup(11, GPIO.OUT)
    servo3 = GPIO.PWM(11, 50)
    servo3.start(0)

    # Finger 4
    GPIO.setup(11, GPIO.OUT)
    servo4 = GPIO.PWM(11, 50)
    servo4.start(0)

    # Finger 5 (THUMB)
    GPIO.setup(11, GPIO.OUT)
    servo5 = GPIO.PWM(11, 50)
    servo5.start(0)

    var = True
    count = 1
    while var:
        count+=1
        servo1.ChangeDutyCycle(var[0])
        servo2.ChangeDutyCycle(var[1])
        servo3.ChangeDutyCycle(var[2])
        servo4.ChangeDutyCycle(var[3])
        servo5.ChangeDutyCycle(var[4])

        time.sleep(2)

        servo1.ChangeDutyCycle(2)
        servo2.ChangeDutyCycle(2)
        servo3.ChangeDutyCycle(2)
        servo4.ChangeDutyCycle(2)
        servo5.ChangeDutyCycle(2)
        if count==numberOfCycles:
            var = False

def number1():
    tempVar = angV.getAngle('1')
    print('1')
    setWrist(tempVar, 1)
    
def number2():
    tempVar = angV.getAngle('2')
    print('2')
    setWrist(tempVar, 1)

def number3():
    tempVar = angV.getAngle('3')
    print('3')
    setWrist(tempVar, 1)


def number4():
    tempVar = angV.getAngle('4')
    print('4')
    setWrist(tempVar, 1)


def number5():
    tempVar = angV.getAngle('5')
    print('5')
    setWrist(tempVar, 1)


def number6():
    tempVar = angV.getAngle('6')
    print('6')
    setWrist(tempVar, 1)


def number7():
    tempVar = angV.getAngle('7')
    print('7')
    setWrist(tempVar, 1)


def number8():
    tempVar = angV.getAngle('8')
    print('8')
    setWrist(tempVar, 1)


def number9():
    tempVar = angV.getAngle('9')
    print('9')
    setWrist(tempVar, 1)


def letterA():
    # tempVar = angV.getAngle('A')
    print('A')
    # setWrist(tempVar, 1)


def letterB():
    tempVar = angV.getAngle('B')
    print('B')
    setWrist(tempVar, 1)


def letterC():
    tempVar = angV.getAngle('C')
    print('C')
    setWrist(tempVar, 1)


def letterD():
    tempVar = angV.getAngle('D')
    print('D')
    setWrist(tempVar, 1)


def letterE():
    tempVar = angV.getAngle('E')
    print('E')
    setWrist(tempVar, 1)


def letterF():
    tempVar = angV.getAngle('F')
    print('F')
    setWrist(tempVar, 1)


def letterG():
    tempVar = angV.getAngle('G')
    print('G')
    setWrist(tempVar, 1)


def letterH():
    tempVar = angV.getAngle('H')
    print('H')
    setWrist(tempVar, 1)


def letterI():
    tempVar = angV.getAngle('I')
    print('I')
    setWrist(tempVar, 1)


def letterJ():
    tempVar = angV.getAngle('J')
    print('J')
    setWrist(tempVar, 1)


def letterK():
    tempVar = angV.getAngle('K')
    print('K')
    setWrist(tempVar, 1)


def letterL():
    tempVar = angV.getAngle('L')
    print('L')
    setWrist(tempVar, 1)


def letterM():
    tempVar = angV.getAngle('M')
    print('M')
    setWrist(tempVar, 1)


def letterN():
    tempVar = angV.getAngle('N')
    print('N')
    setWrist(tempVar, 1)


def letterO():
    tempVar = angV.getAngle('O')
    print('O')
    setWrist(tempVar, 1)


def letterP():
    tempVar = angV.getAngle('P')
    print('P')
    setWrist(tempVar, 1)


def letterQ():
    tempVar = angV.getAngle('Q')
    print('Q')
    setWrist(tempVar, 1)


def letterR():
    tempVar = angV.getAngle('R')
    print('R')
    setWrist(tempVar, 1)


def letterS():
    tempVar = angV.getAngle('S')
    print('S')
    setWrist(tempVar, 1)


def letterT():
    tempVar = angV.getAngle('T')
    print('T')
    setWrist(tempVar, 1)


def letterU():
    tempVar = angV.getAngle('U')
    print('U')
    setWrist(tempVar, 1)


def letterV():
    tempVar = angV.getAngle('V')
    print('V')
    setWrist(tempVar, 1)


def letterW():
    tempVar = angV.getAngle('W')
    print('W')
    setWrist(tempVar, 1)


def letterX():
    tempVar = angV.getAngle('X')
    print('X')
    setWrist(tempVar, 1)


def letterY():
    tempVar = angV.getAngle('Y')
    print('Y')
    setWrist(tempVar, 1)


def letterZ():
    tempVar = angV.getAngle('Z')
    print('Z')
    setWrist(tempVar, 1)


def wordHello():
    tempVar = angV.getAngle("HELLO")
    print("Hello")
    setWrist(tempVar, 2)


def wordOkay():
    tempVar = angV.getAngle("OK")
    print("Okay")
    setWrist(tempVar, 1)


def wordBye():
    tempVar = angV.getAngle("BYE")
    print("Bye")
    setWrist(tempVar, 3)
