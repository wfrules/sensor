import RPi.GPIO as GPIO
led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)


def hign():
    GPIO.output(led, GPIO.HIGH)
    print('high')
def low():
    GPIO.output(led, GPIO.LOW)
    print('low')
try:
    while True:
      reply = input('enter text:')
      if reply=='h':
          hign()
      elif reply=='l':
          low()
      elif reply=='s':
          break
except KeyboardInterrupt as results:
        print(results)
finally:
    print("结束")
    GPIO.cleanup()