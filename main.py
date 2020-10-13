from machine import Pin, PWM, ADC
from time import sleep_ms

SERVO1_MIN = 22
SERVO1_MAX = 125
SERVO1_MID = (SERVO1_MAX + SERVO1_MIN) / 2


SERVO2_MIN = 22
SERVO2_MAX = 125
SERVO2_MID = (SERVO2_MAX + SERVO2_MIN) / 2

SERVO3_MIN = 22
SERVO3_MAX = 125
SERVO3_MID = (SERVO3_MAX + SERVO3_MIN) / 2

servo1 = PWM(Pin(21))
servo1.freq(50)

servo2 = PWM(Pin(22))
servo2.freq(50)

servo3 = PWM(Pin(23))
servo3.freq(50)


pot1 = ADC(Pin(34))
pot1.atten(ADC.ATTN_11DB)
pot1.width(ADC.WIDTH_9BIT)

pot2 = ADC(Pin(32))
pot2.atten(ADC.ATTN_11DB)
pot2.width(ADC.WIDTH_9BIT)

pot3 = ADC(Pin(33))
pot3.atten(ADC.ATTN_11DB)
pot3.width(ADC.WIDTH_9BIT)

while 1:
    dutyS1 = int(SERVO1_MIN + ((SERVO1_MAX - SERVO1_MIN) / 512) * pot1.read())
    degree1 = int((180 / (SERVO1_MAX - 1 - SERVO1_MIN)) * (dutyS1 - SERVO1_MIN))
    servo1.duty(dutyS1)

    dutyS2 = int(SERVO2_MIN + ((SERVO2_MAX - SERVO2_MIN) / 512) * pot2.read())
    degree2 = int((180 / (SERVO2_MAX - 1 - SERVO2_MIN)) * (dutyS2 - SERVO2_MIN))
    servo2.duty(dutyS2)

    dutyS3 = int(SERVO3_MIN + ((SERVO3_MAX - SERVO3_MIN) / 512) * pot3.read())
    degree3 = int((180 / (SERVO3_MAX - 1 - SERVO3_MIN)) * (dutyS3 - SERVO3_MIN))
    servo3.duty(dutyS3)

    print(degree1, degree2, degree3)
    sleep_ms(10)
