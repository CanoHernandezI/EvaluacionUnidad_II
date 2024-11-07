from machine import Pin, PWM, time_pulse_us
from time import sleep

led1 = Pin(26, Pin.OUT)
led2 = Pin(27, Pin.OUT)

trigger = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN)

servo1 = PWM(Pin(12), freq=50)
servo2 = PWM(Pin(13), freq=50) 

def mover_servo(servo, angulo):
    duty = int((angulo / 180.0) * 102 + 26) 
    servo.duty(duty)

def medir_distancia():
    trigger.off()
    sleep(0.000002)
    trigger.on()
    sleep(0.00001)
    trigger.off()
    
    duracion = time_pulse_us(echo, 1)
    
    distancia = (duracion / 2) * 0.0343
    return distancia

while True:
    distancia = medir_distancia()
    print("Distancia medida:", distancia, "cm")
    
    if distancia <= 5:
        led1.on()
        led2.on()
        print("Objeto cercano, LEDs encendidos")

        mover_servo(servo1, 60)
        mover_servo(servo2, 60)
        sleep(0.3)  
        mover_servo(servo1, 0)
        mover_servo(servo2, 0)
        sleep(0.5) 
    else:
        led1.off()
        led2.off()
        print("No hay objeto cercano, LEDs apagados")

    sleep(0.3)


