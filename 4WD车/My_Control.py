#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

#小车电机引脚定义
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)

#忽略警告信息
GPIO.setwarnings(False)

Ser_x = 11
Ser_y = 9
Ser_f = 23
EchoPin=0
TrigPin=1
Led_R = 22
Led_G = 27
Led_b = 24


#电机引脚初始化操作
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global pwm_ser_x
    global pwm_ser_y
    global pwm_ser_f
    global delaytime
    GPIO.setup(Led_R,GPIO.OUT)
    GPIO.setup(Led_G,GPIO.OUT)
    GPIO.setup(Led_B,GPIO.OUT)
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)
    GPIO.setup(Ser_x,GPIO.OUT)
    GPIO.setup(Ser_y,GPIO.OUT)
    GPIO.setup(Ser_f,GPIO.OUT)
    pwm_ser_x = GPIO.PWM(Ser_x,50)
    pwm_ser_y = GPIO.PWM(Ser_y,50)
    pwm_ser_f = GPIO.PWM(Ser_f,50)
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #设置pwm引脚和频率为2000hz
    
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    pwm_ser_x.start(0)
    pwm_ser_y.start(0)
    pwm_ser_f.start(0)
    

#小车前进	
def run(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车后退
def back(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车左转	
def left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车右转
def right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车原地左转
def spin_left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车原地右转
def spin_right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车停止	
def brake(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

def servo_appoint_x(pos):
    for i in range(18):
        pwm_ser_x.ChangeDutyCycle(2.5+10*pos/180)

def servo_appoint_y(pos):
    for i in range(18):
        pwm_ser_y.ChangeDutyCycle(2.5+10*pos/180)
def servo_appoint_f(pos):
    for i in range(18):
        pwm_ser_f.ChangeDutyCycle(2.5+10*pos/180)

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


#try/except语句用来检测try语句块中的错误，
#从而让except语句捕获异常信息并处理。
#小车循环前进1s，后退1s，左转2s，右转2s，原地左转3s
#原地右转3s，停止1s。
motor_init()
while True:
    a = input("Please Input : ")
    if(a==12):
        while True:
            c = input('Please input 5 to end! :')
            GPIO.output(LED_R, GPIO.HIGH)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_B, GPIO.LOW)
            time.sleep(1)
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.HIGH)
            GPIO.output(LED_B, GPIO.LOW)
            time.sleep(1)
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_B, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_R, GPIO.HIGH)
            GPIO.output(LED_G, GPIO.HIGH)
            GPIO.output(LED_B, GPIO.LOW)
            time.sleep(1)
            GPIO.output(LED_R, GPIO.HIGH)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_B, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.HIGH)
            GPIO.output(LED_B, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_B, GPIO.LOW)
            time.sleep(1)
            if(c==5):
                break
                
            
    if(a==9):
        while True:
            b=input('Please input 1~3 : ')
            if(b>4):
                break
            if(b==1):
                while True:
                    c=input('Please input 0~180: ')
                    if(c==181):
                        break
                    servo_appoint_x(c)
            if(b==2):
                while True:
                    c=input('Please input 0~180: ')
                    if(c==181):
                        break
                    servo_appoint_y(c)
            if(b==3):
                while True:
                    
                    c=input('Please input 0~180: ')
                    Distance_test()
                    if(c==181):
                        break
                    servo_appoint_f(c)
            
            
    if(a==2):
        run(1)
    if(a==8):
        back(1)
    if(a==4):
        spin_left(1)
    if(a==6):
        spin_right(1)
    if(a==5):
        brake(1)
    if(a==11):
        GPIO.setup(2,GPIO.OUT)
        time.sleep(3)
        GPIO.setup(2,GPIO.IN)
    
    

#try:
#    motor_init()
#    while True:
#        run(1)
#	back(1)
#	left(2)
#	right(2)
#	spin_left(3)
#	spin_right(3)
#	brake(1)
#except KeyboardInterrupt:
#    pass
pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup() 

