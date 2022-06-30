# from machine import Pin as pin
# from utime import sleep, sleep_ms
# led1=pin(2,pin.OUT)
# pausa=0.2
# while True:
#   led1.value(1)
#   sleep(pausa)
#   led1.value(0)
#   sleep(pausa)
from machine import Pin as pin
from utime import sleep, sleep_ms
led1=pin(2,pin.OUT)
pul_a=pin(15,pin.IN,pin.PULL_UP)
pul_b=pin(14,pin.IN,pin.PULL_UP)
pausa=0.2
def correo():
    led1.value(1)
    sleep(pausa)
    led1.value(0)
    sleep(pausa)
while True:
    if not pul_a.value():
        correo()