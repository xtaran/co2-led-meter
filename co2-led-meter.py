#!/usr/bin/env python3

# Copyright 2017, 2018 Pimoroni Ltd.
# Copyright 2022 Axel Beckert <abe@deuxchevaux.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

from scd4x import SCD4X
import colorsys
import math
import ledshim

# Config
max_ppm = 1500
hue_range = 140
hue_start = -40
max_brightness = 0.6

# Init
device = SCD4X(quiet=True)
device.start_periodic_measurement()
ledshim.set_clear_on_exit()

# Functions
def show_graph(v):
    v *= ledshim.NUM_PIXELS
    for x in range(ledshim.NUM_PIXELS):
        hue = ((hue_start + ((x / float(ledshim.NUM_PIXELS)) * hue_range)) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        if v < 0:
            brightness = min(-v, 1.0) * max_brightness
        else:
            brightness = 0

        ledshim.set_pixel(x, r, g, b, brightness)
        v -= 1

    ledshim.show()

# Main loop
try:
    while True:
        co2, temperature, relative_humidity, timestamp = device.measure()
        print(f"""{co2:.1f}""")

        v = 1-(min(co2,max_ppm)/max_ppm)             # Get a value between 0 and 1
        show_graph(v)  # Use it as the pixel index

except KeyboardInterrupt:
    pass
