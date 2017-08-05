import RPi.GPIO as GPIO


class Led:
    def __init__(self, led_pin, initial_value=False):
        self._led_pin = led_pin
        GPIO.setup(self._led_pin, GPIO.OUT)
        GPIO.output(self._led_pin, initial_value)

    def on(self):
        GPIO.output(self._led_pin, True)

    def off(self):
        GPIO.output(self._led_pin, False)
