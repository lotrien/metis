import RPi.GPIO as GPIO
import yaml
import argparse

from metis import motion, camera, led, telegram


def parse_command_line():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--conf', default='config.yaml',
        help='set path to the config file')

    arguments = parser.parse_args()

    return arguments

if __name__ == '__main__':
    with open(parse_command_line().conf, 'r') as stream:
        config = yaml.load(stream)

    GPIO.setmode(GPIO.BCM)

    detector = motion.MotionDetector(config['pins']['motion_sensor'])
    recorder = camera.CamRecorder()
    motion_led = led.Led(config['pins']['led_motion_on'])
    no_motion_led = led.Led(config['pins']['led_motion_off'], True)

    detector.start.connect(lambda sender: motion_led.on(), weak=False)
    detector.start.connect(lambda sender: no_motion_led.off(), weak=False)
    detector.start.connect(lambda sender: recorder.record(), weak=False)

    detector.end.connect(lambda sender: motion_led.off(), weak=False)
    detector.end.connect(lambda sender: no_motion_led.on(), weak=False)
    detector.end.connect(lambda sender: recorder.stop(), weak=False)

    recorder.end.connect(lambda sender, filename: print(filename, 'recorded'), weak=False)

    if 'telegram' in config:
        telega = telegram.Telegram(config['telegram']['token'], config['telegram']['recipient'])
        detector.start.connect(lambda sender: telega.send_message('Intruder detected'), weak=False)
        recorder.end.connect(lambda sender, filename: telega.send_doc(filename), weak=False)

    try:
        detector.run()
    except (KeyboardInterrupt, SystemExit):
        print('Exiting')
    finally:
        motion_led.off()
        no_motion_led.off()
        GPIO.cleanup()
