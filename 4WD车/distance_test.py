import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
EchoPin = 0
TrigPin = 1
GPIO.setwarnings(False)
def init():
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)

def Distance_test():
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1=time.time()
    while GPIO.input(EchoPin):
        pass
    t2=time.time()
    print "distance is %d" % (((t2 - t1)* 340 / 2) * 100)
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100

distance = Distance_test()
print(distance)
    
