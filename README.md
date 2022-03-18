CO₂ LED Meter
=============

This is the (rather trivial) code for a simple LED-based CO₂ light
meter (more or less a continuous CO₂ "traffic light") based on the
following hardware components:

* A [Raspberry Pi](https://www.raspberrypi.com/) or similar single
  board computer (SBC) with a 40-pin GPIO bar. In my case I used an
  older Raspberry Pi 2B with an matte-black Pibow Midnight (Coupé)
  case which I bought in 2017 from Pimoroni.

* The [Pimoroni LED Shim](https://shop.pimoroni.com/products/led-shim)
  as LED bar.

* The [Pimoroni SCD41 CO₂ Sensor
  Breakout](https://shop.pimoroni.com/products/scd41-co2-sensor-breakout)
  as CO₂ sensor.

* One of following as socket for the CO₂ Sensor Breakout:

  * the [Pimoroni Breakout Garden Mini (I2C)
	pHAT](https://shop.pimoroni.com/products/breakout-garden-mini-i2c),

  * the [Breakout Garden Mini (I2C+SPI)
	pHAT](https://shop.pimoroni.com/products/breakout-garden-mini-i2c-spi), or

  * the bigger [Breakout Garden
	HAT](https://shop.pimoroni.com/products/breakout-garden-hat).

* Optionally the [Waveshare Raspberry Pi 400 GPIO Header
  Adapter](https://www.waveshare.com/pi400-gpio-adapter-a.htm) to on
  the one hand turn the pHAT or HAT vertical (so I don't have to setup
  the Raspberry Pi vertically) and on the other hand allow to mount
  the LED Shim even if a case is used which encloses the GPIO pins to
  some height.


Code Base
---------

The code in here is heavily based on two example scripts from
Pimoroni's LED Shim and SCD4x Python libraries (which are needed
anyways, too), namely on:

* [scd4x-python/examples/basic.py](https://github.com/pimoroni/scd4x-python/blob/main/examples/basic.py)
* [led-shim/examples/gradient_graph.py](https://github.com/pimoroni/led-shim/blob/master/examples/gradient_graph.py)


License
-------

Since the code is heavily based on two scripts published under the MIT
License, this code is licensed under the [MIT License](LICENSE) as
well.


Copyright
---------

* Copyright 2017, 2018 Pimoroni Ltd.
* Copyright 2022 Axel Beckert
