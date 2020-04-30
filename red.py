#!/usr/bin/python
#-*- coding: utf-8 -*-
import time
import signal
import RPi.GPIO as GPIO
import os

stop = False
  
  
def keyboard_handler(signum, frame): 
  global stop
  print('stop') 
  stop = True

signal.signal(signal.SIGABRT, keyboard_handler) 


GPIO.setmode(GPIO.BCM) #使用BCM编码方式

#定义引脚

GPIO_OUT = 23
led = 18

#设置23针脚为输入，接到红外避障传感器模块的out引脚
GPIO.setup(GPIO_OUT,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

def warn(signal): #亮灯来作为有障碍物时发出的警告
    localtime = time.asctime( time.localtime(time.time()) )
    # print("current time: ", signal)
    GPIO.output(led,signal)
    # GPIO.output(led,GPIO.HIGH)
    # time.sleep(0.5)
    # GPIO.output(led,GPIO.LOW)
    # time.sleep(0.5)

while not stop:
    signal = GPIO.input(GPIO_OUT);
    # if GPIO.input(GPIO_OUT)==0: #当有障碍物时，传感器输出低电平，所以检测低电平
    warn(signal)  

print('clean up')          
GPIO.cleanup()