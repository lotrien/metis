import datetime

import picamera
import blinker


class CamRecorder:

    start = blinker.Signal()
    end = blinker.Signal()

    def __init__(self):
        self._camera = picamera.PiCamera()
        self._camera.vflip = True
        self._camera.hflip = True

    def record(self):
        self._filename = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
        self._camera.start_recording(self._filename)

        self.start.send(self, filename=self._filename)

    def stop(self):
        self._camera.stop_recording()

        self.end.send(self, filename=self._filename)
