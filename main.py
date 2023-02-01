from modules.gpio_wrapper import GpioWrapper
import time

unit = 1
r1 = 0
y1 = 0
g1 = 0
r2 = 0
y2 = 0
g2 = 0

gpio = GpioWrapper(r1, y1, g1, r2, y2, g2)
gpio.red1_on()
gpio.red2_on()

while True:
    gpio.red1_off()
    gpio.yellow1_on()
    time.sleep(unit)

    gpio.yellow1_off
    gpio.green1_on()
    time.sleep(unit * 5)

    gpio.green1_off()
    gpio.yellow1_on()
    time.sleep(unit)

    gpio.yellow1_off()
    gpio.red1_on()
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