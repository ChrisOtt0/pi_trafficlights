import RPi.GPIO as GPIO

class GpioWrapper:
    gpio = GPIO
    portr1 = 0
    porty1 = 0
    portg1 = 0

    portr2 = 0
    porty2 = 0
    portg2 = 0

    def __init__(self, portr1, porty1, portg1, portr2, porty2, portg2):
        self.gpio.setmode(GPIO.BCM)
        self.portr1 = portr1
        self.porty1 = porty1
        self.portg1 = portg1

        self.portr2 = portr2
        self.porty2 = porty2
        self.portg2 = portg2

        self.gpio.setup(self.portr1, GPIO.OUT)
        self.gpio.setup(self.porty1, GPIO.OUT)
        self.gpio.setup(self.portg1, GPIO.OUT)
        self.gpio.setup(self.portr2, GPIO.OUT)
        self.gpio.setup(self.porty2, GPIO.OUT)
        self.gpio.setup(self.portg2, GPIO.OUT)

    def red1_on(self):
        self.gpio.output(self.portr1, True)

    def red1_off(self):
        self.gpio.output(self.portr1, False)

    def yellow1_on(self):
        self.gpio.output(self.porty1, True)

    def yellow1_off(self):
        self.gpio.output(self.porty1, False)

    def green1_on(self):
        self.gpio.output(self.portg1, True)

    def green1_off(self):
        self.gpio.output(self.portg1, False)

    def red2_on(self):
        self.gpio.output(self.portr2, True)

    def red2_off(self):
        self.gpio.output(self.portr2, False)

    def yellow2_on(self):
        self.gpio.output(self.porty2, True)

    def yellow2_off(self):
        self.gpio.output(self.porty2, False)

    def green2_on(self):
        self.gpio.output(self.portg2, True)

    def green2_off(self):
        self.gpio.output(self.portg2, False)

