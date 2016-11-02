#!/usr/bin/python
from __future__ import division
import spidev
import time
import os
import math
import sys

global reading1
reading1 = False
global reading2
reading2 = False

# open spi port:
spi = spidev.SpiDev()
spi.open(0,0)


def ReadChannel(channel):    # read data from mcp2008; channel must be integer 0 - 7
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data 


while True:  # always loop

	reading2 = ReadChannel(1) # volume control

	ditherfactor = int(reading2 / 50) + 1	
	if ((reading2 < reading1 - ditherfactor) or (reading2 > reading1 + ditherfactor)):
		reading3 = int(math.log((reading2 + 1),10) * 33) + 1
		print reading3
		reading1 = reading2 
		time.sleep(1)
		if reading3 > 90:
			os.popen("espeak 'low battery' 2>/dev/null")
			sys.exit()
