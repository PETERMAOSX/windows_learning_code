import RPi.GPIO as GPIO
import time
import string
import serial

#小车电机
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#小车上面的k2按钮
key = 8

#超声波
EchoPin = 0
TrigPin = 1

#RGB三色灯
LED_R = 22
LED_G = 27
LED_B = 24

#舵机
ServoPin = 23

#红外避障
AvoidSensorLeft = 12
AvoidSensorRight = 17

#峰鸣器
buzzer = 8

#灭火器
OutfirePin = 2

#寻迹
TrackSensorLeftPin1 = 3 #定义左边第一个为3口
TrackSensorLeftPin2 = 5 #定义左边第二个为5口
TrackSensorRightPin1 = 4 #定义右边第一个为4口
TrackSensorRightPin2 = 18 #定义右边第二个为18口

#光敏电阻引脚定义
LdrSensorLeft = 7
LdrSensorLeft = 6

#串口计时全局变量定义
global timecount 
global count

#设置GPIO口为BCM编码模式
GPIO.setmode(GPIO.BCM)

#忽略警告信息
GPIO.setwarings(False)

#电机初始化为输出模式
#按键引脚初始化为输入模式
#超声波，RGB三色灯，舵机初始化
#红外避障初始化
def init():
    global pwm_ENA
    global pwm_ENB
    global pwm_servo
    global pwm_rled
    global pwm_gled
    global pwm_bled
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(key,GPIO.IN)
    GPIO.setup(buzzer,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(OutfirePin,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.IN)
    GPIO.setup(LED_R,GPIO.OUT)
    GPIO.setup(LED_G,GPIO.OUT)
    GPIO.setup(LED_B,GPIO.OUT)
    GPIO.setup(ServoPin,GPIO.OUT)
    GPIO.setup(AvoidSensorLeft,GPIO.IN)
    GPIO.setup(AvoidSensorRight,GPIO.IN)
    GPIO.setup(LdrSensorLeft,GPIO.IN)
    GPIO.setup(LdrSensorRight,GPIO.IN)
    GPIO.setup(TrackSensorLeftPin1,GPIO.IN)
    GPIO.setup(TrackSensorLeftPin2,GPIO.IN)
    GPIO.setup(TrackSensorRightPin1,GPIO.IN)
    GPIO.setup(TrackSensorRightPin2,GPIO.IN)
    #设置pwm引脚和频率为2000hz
    pwm_ENA = GPIO.PWM(ENA,2000)
    pwm_ENB = GPIO.PWM(ENB,2000)
    pwm_ENA.start(0)
    pwm_ENA.start(0)
    #设置舵机的频率和起始占空比
    pwm_servo = GPIO.PWM(ServoPin,50)
    pwm_servo.start(0)
    pwm_rled = GPIO.PWM(LED_R,1000)
    pwm_gled = GPIO.PWM(LED_G,1000)
    pwm_bled = GPIO.PWM(LED_G,1000)
    pwm_rled.start(0)
    pwm_gled.start(0)
    pwm_bled.start(0)
    
    
#小车前进
def run(leftspeed,rightspeed):
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


#小车后退
def back(leftspeed,rightspeed):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)

#小车左转
def left(leftspeed,rightspeed):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    
    
#小车右转
def right(leftspeed,rightspeed):
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    
#小车停止
def brake():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)


#小车原地左转
def spin_left(leftspeed,rightspeed):
    GPIO.output(IN1,LOW)
    GPIO.output(IN2,HIGH)
    GPIO.output(IN3,HIGH)
    GPIO.output(IN4,LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    
#小车原地右转
def spin_right():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGHs)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    
    
#按键检测
def keyscan():
    while GPIO.input(key):
        pass
    while not GPIO.input(key):
        time.sleep(0.01)
        if not GPIO.input(key):
            time.sleep(0.01)
            while not GPIO.input(key):
                pass
   
   
#超声波函数1
def Distance_test():
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100

#舵机转到指定角度
def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5+10*pos/180)
        
 
#舵机旋转到超声波测距避障，led根据车的状态显示相应的颜色
def servo_color_carstate():
    #开红灯
    GPIO.setup(LED_R,GPIO.HIGH)
    GPIO.setup(LED_G,GPIO.LOW)
    GPIO.setup(LED_B,GPIO.LOW)
    back(20,20)
    time.sleep(0.08)
    brake()
    
    #舵机旋转到0度，就是右侧，测距
    servo_appointed_detection(0)
    time.sleep(0.8)
    rightdistance = Distance_test()
    
    #舵机旋转到180度，即左侧，测距
    servo_appointed_detection(180)
    time.sleep(0.8)
    leftdistance = Distance_test()
    
    #舵机旋转到90度，即正中央，测距
    servo_appointed_detection(90)
    time.sleep(0.8)
    frontdistance = Distance_test()
    
    if(leftdistance<30 and rightdistance<30 and frontdistance<30):
        #亮红色，掉头
        GPIO.output(LED_R,GPIO.HIGH)
        GPIO.output(LED_G,GPIO.LOW)
        GPIO.output(LED_B,GPIO.HIGH)
        back(25,25)
        time.sleep(0.58)
    elif leftdistance>=rightdistance:
        #亮蓝色,向左转
        GPIO.output(LED_R,GPIO.LOW)
        GPIO.output(LED_G,GPIO.LOW)
        GPIO.output(LED_B,GPIO.HIGH)
        spin_left(25,25)
        time.sleep(0.28)
    elif leftdistance <=rightdistance:
        #亮品红色，向右转
        GPIO.output(LED_R,GPIO.HIGH)
        GPIO.output(LED_G,GPIO.LOW)
        GPIO.output(LED_B,GPIO.HIGH)
        spin_right(25,25)
        time.sleep(0.28)

#巡线测试
#def tracking_test():
#    global infrared_track_value
#    #检测到黑线时候寻迹模块相应的指示灯亮，端口电平为LOW
    #未检测到黑线时候寻迹模块相应的指示灯没有亮，端口电平为HIGH
#    TrackSensorLeftValue1 = GPIO.input(TrackSensorLeftPin1)
#    TrackSensorLeftValue2 = GPIO.input(TrackSensorLeftPin2)
#   TrackSensorRightValue1 = GPIO.input(TrackSensorRightPin1)
#   TrackSensorRightValue2 = GPIO.input(TrackSensorRightPin2)
    
#    infrared_track_value_list = ['0','0','0','0']
#    infrared_track_value_list[0] = str(1^ TrackSensorLeftValue1)
#    infrared_track_value_list[1] = str(1^ TrackSensorLeftValue2)
#    infrared_track_value_list[2] = str(1^ TrackSensorRightValue1)
#    infrared_track_value_list[3] = str(1^ TrackSensorRightValue2)
#   infrared_track_value = ''.join(infrared_track_value_list)
    
    
#延时
time.sleep(2)
    
try:
    init()
    keyscan()
    a = input("输入一个模式")
    if a=='a' :
        while True:  #首先使用的是红外避障，当距离小于30后才调用超声波避障
        distance = Distance_test()
        if distance>50:
            LeftSensorValue = GPIO.input(AvoidSensorLeft)
            RightSensorValue = GPIO.input(AvoidSensorRight)
                if LeftSensorValue == True and RightSensorValue == True :
                    run(30,30)
                elif LeftSensorValue == True and RightSensorValue == False:
                    spin_left(25,25)
                    time.sleep(0.02)
                elif LeftSensorValue == False and RightSensorValue == True:
                    spin_right(25,25)
                    time.sleep(0.02)
                elif LeftSensorValue == False and RightSensorValue == False:
                    spin_right(25,25)
                    time.sleep(0.002)
                    run(30,30)
                    GPIO.output(LED_R,GPIO.LOW)
                    GPIO.output(LED_G,GPIO.HIGH)
                    GPIO.output(LED_G,GPIO.LOW)
        elif 30<=distance<=50 :
            LeftSensorValue = GPIO.input(AvoidSensorLeft)
            RightSensorValue = GPIO.input(AvoidSensorRight)
            if LeftSensorValue == True and RightSensorValue == True :
                run(30,30)
            elif LeftSensorValue == True and RightSensorValue == False:
                spin_left(25,25)
                time.sleep(0.002)
            elif LeftSensorValue == False and RightSensorValue == True:
                spin_right(25, 25)
                time.sleep(0.002)
            elif LeftSensorValue == False and RightSensorValue == False:
                spin_right(25,25)
                time.sleep(0.002)
                run(25,25)
        elif distance < 30 :
            servo_color_carstate()
    if a=='b':
        while True:
            #遇到光线,寻光模块的指示灯灭,端口电平为HIGH
            #未遇光线,寻光模块的指示灯亮,端口电平为LOW
            LdrSersorLeftValue  = GPIO.input(LdrSensorLeft);
            LdrSersorRightValue = GPIO.input(LdrSensorRight);

            if LdrSersorLeftValue == True and LdrSersorRightValue == True :
                run()             #两侧均有光时信号为HIGH，光敏电阻指示灯灭,小车前进
            elif LdrSersorLeftValue == True and LdrSersorRightValue == False :
                spin_left()       #左边探测到有光，有信号返回，向左转
                time.sleep(0.002)
            elif LdrSersorRightValue == True and LdrSersorLeftValue == False:
                spin_right()      #右边探测到有光，有信号返回，向右转
                time.sleep(0.002)
            elif LdrSersorRightValue == False and LdrSersorLeftValue == False :
                brake()           #均无光，停止
    if a=='c':
        while True:
            #检测到黑线时循迹模块相应的指示灯亮，端口电平为LOW
            #未检测到黑线时循迹模块相应的指示灯灭，端口电平为HIGH
            TrackSensorLeftValue1  = GPIO.input(TrackSensorLeftPin1)
            TrackSensorLeftValue2  = GPIO.input(TrackSensorLeftPin2)
            TrackSensorRightValue1 = GPIO.input(TrackSensorRightPin1)
            TrackSensorRightValue2 = GPIO.input(TrackSensorRightPin2)

            #四路循迹引脚电平状态
            # 0 0 X 0
            # 1 0 X 0
            # 0 1 X 0
            #以上6种电平状态时小车原地右转
            #处理右锐角和右直角的转动
            if (TrackSensorLeftValue1 == False or TrackSensorLeftValue2 == False) and  TrackSensorRightValue2 == False:
                spin_right(100, 100)
                time.sleep(0.08)
 
            #四路循迹引脚电平状态
            # 0 X 0 0       
            # 0 X 0 1 
            # 0 X 1 0       
            #处理左锐角和左直角的转动
            elif TrackSensorLeftValue1 == False and (TrackSensorRightValue1 == False or  TrackSensorRightValue2 == False):
                spin_left(100, 100)
                time.sleep(0.08)
  
            # 0 X X X
            #最左边检测到
            elif TrackSensorLeftValue1 == False:
                spin_left(80, 80)
     
            # X X X 0
            #最右边检测到
            elif TrackSensorRightValue2 == False:
                spin_right(80, 80)
   
            #四路循迹引脚电平状态
            # X 0 1 X
            #处理左小弯
            elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == True:
                left(0,90)
   
            #四路循迹引脚电平状态
            # X 1 0 X  
            #处理右小弯
            elif TrackSensorLeftValue2 == True and TrackSensorRightValue1 == False:
                right(90, 0)
   
            #四路循迹引脚电平状态
            # X 0 0 X
            #处理直线
            elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == False:
                run(100, 100)
   
            #当为1 1 1 1时小车保持上一个小车运行状态
    if a=='d':
        GPIO.output(OutfirePin,not GPIO.input(OutfirePin) )
        
except KeyboardInterrupt:
    pass
pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup()