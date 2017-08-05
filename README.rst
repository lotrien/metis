Metis
=====

Metis is an application to make your home a safer place to live by watching and
recording any movements. It also (optionally) supports notifications via
Telegram. 


Requirements
------------

* `Raspberry Pi 3`_
* `HC-SR501 PIR Motion Sensor`_
* `Raspberry Pi Camera Board v2`_
* 2 LEDs

.. _HC-SR501 PIR Motion Sensor: http://henrysbench.capnfatz.com/henrys-bench/arduino-sensors-and-input/arduino-hc-sr501-motion-sensor-tutorial/
.. _Raspberry Pi 3: https://en.wikipedia.org/wiki/Raspberry_Pi
.. _Raspberry Pi Camera Board v2: https://www.adafruit.com/product/3099


Quickstart
----------

1. Install Metis:

   .. code:: bash

      $ pip install metispi

2. Run Metis:

   .. code:: bash

      $ [sudo] python -m metis --conf=path/to/config.yaml

   .. note:: Based on Linux you use, you may or may not need root privileges to run Metis.



Configuration
-------------

It's mandatory to pass a config file because some of the options are required.
Here's an example:

.. code:: yaml

   pins:
     motion_sensor:   4  # pin number HC-SR501 attached to
     led_motion_on:  17  # pin number LED "motion detected" attached to
     led_motion_off: 20  # pin number LED "no motions" attached to
   telegram:
     token: XXXXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
     recipient: 000000001

One more thing, a whole ``telegram`` node is optional and may be omitted if you
are not interested in notifications via Telegram. If you do, you need to create
a Telegram bot and pass its token as ``telegram.token`` option.
