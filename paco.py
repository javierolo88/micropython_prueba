from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
ledc=pin(2,pin.OUT);ledb=pin(19,pin.OUT);leda=pin(23,pin.OUT);sensor=pin(15,pin.IN)
def print_led(a,b,c):
  leda.value(a)
  ledb.value(b)
  ledc.value(c)
  pausam(130)
def secuencia():
    print_led(0,0,0)
    print_led(0,0,1)
    print_led(0,1,0)
    print_led(1,0,0)
    print_led(0,0,0)
while True: 
  if not sensor.value():
    print (f"saca la secuencia")
    secuencia()
