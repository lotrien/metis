import gpiozero
import blinker


class MotionDetector:

    start = blinker.Signal()
    end = blinker.Signal()

    def __init__(self, pin):
        self._sensor = gpiozero.MotionSensor(pin)

    def run(self):
        while True:
            self._sensor.wait_for_motion()
            self.start.send(self)

            self._sensor.wait_for_no_motion()
            self.end.send(self)
