import machine
from time import sleep
led1=machine.Pin(2, machine.Pin.OUT)
led2=machine.Pin(4, machine.Pin.OUT)
led3=machine.Pin(5, machine.Pin.OUT)
led4=machine.Pin(18, machine.Pin.OUT)
led5=machine.Pin(19, machine.Pin.OUT)
led6=machine.Pin(21, machine.Pin.OUT)
led7=machine.Pin(22, machine.Pin.OUT)
led8=machine.Pin(23, machine.Pin.OUT)
led9=machine.Pin(13, machine.Pin.OUT)
led10=machine.Pin(12, machine.Pin.OUT)
while True:
    led1.on()
    sleep(0.1)
    led1.off()
    led2.on()
    sleep(0.1)
    led2.off()
    led3.on()
    sleep(0.1)
    led3.off()
    led4.on()
    sleep(0.1)
    led4.off()
    led5.on()
    sleep(0.1)
    led5.off()
    led6.on()
    sleep(0.1)
    led6.off()
    led7.on()
    sleep(0.1)
    led7.off()
    led8.on()
    sleep(0.1)
    led8.off()
    led9.on()
    sleep(0.1)
    led9.off()
    led10.on()
    sleep(0.1)
    led10.off()
    led9.on()
    sleep(0.1)
    led9.off()
    led8.on()
    sleep(0.1)
    led8.off()
    led7.on()
    sleep(0.1)
    led7.off()
    led6.on()
    sleep(0.1)
    led6.off()
    led5.on()
    sleep(0.1)
    led5.off()
    led4.on()
    sleep(0.1)
    led4.off()
    led3.on()
    sleep(0.1)
    led3.off()
    led2.on()
    sleep(0.1)
    led2.off()
    led1.on()
    sleep(0.1)
    led1.off()


