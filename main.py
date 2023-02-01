from modules.gpio_wrapper import GpioWrapper
import time

unit = 2
r1 = 17
y1 = 5
g1 = 26
r2 = 18
y2 = 24
g2 = 12

gpio = GpioWrapper(r1, y1, g1, r2, y2, g2)
gpio.red1_on()
gpio.red2_on()

while True:
    gpio.red1_off()
    gpio.yellow1_on()
    time.sleep(unit)

    gpio.yellow1_off()
    gpio.green1_on()
    time.sleep(unit * 5)

    gpio.green1_off()
    gpio.yellow1_on()
    time.sleep(unit)

    gpio.yellow1_off()
    gpio.red1_on()
    time.sleep(unit)

    gpio.red2_off()
    gpio.yellow2_on()
    time.sleep(unit)

    gpio.yellow2_off()
    gpio.green2_on()
    time.sleep(unit * 5)

    gpio.green2_off()
    gpio.yellow2_on()
    time.sleep(unit)

    gpio.yellow2_off()
    gpio.red2_on()
    time.sleep(unit)
