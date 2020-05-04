#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import signal
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BCM)  # 使用BCM编码方式

# 定义引脚

GPIO_OUT = 17
led = 18

# 设置23针脚为输入，接到红外避障传感器模块的out引脚
GPIO.setup(GPIO_OUT, GPIO.IN)
GPIO.setup(led,GPIO.OUT)


def warn(signal):  # 亮灯来作为有障碍物时发出的警告
    localtime = time.asctime(time.localtime(time.time()))

    if signal == 0:
        print("high")
        GPIO.output(led,GPIO.HIGH)
    else:
        print("low")
        GPIO.output(led,GPIO.LOW)
    time.sleep(0.5)

try:
    while True:
        signal = GPIO.input(GPIO_OUT);
        # if GPIO.input(GPIO_OUT)==0: #当有障碍物时，传感器输出低电平，所以检测低电平
        warn(signal)
except KeyboardInterrupt as results:
        print(results)
finally:
    print("结束")
    GPIO.cleanup()
