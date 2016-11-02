#!/usr/bin/python
# data logger for power supply voltage monitored on adc 1 through voltage divider

from __future__ import division
import spidev
import time
import os

global reading1
reading1 = False
global reading2
reading2 = False

# open spi port:
spi = spidev.SpiDev()
spi.open(0,0)


def ReadChannel(channel): # channel 2 watches power supply
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data

while True:  # always loop

	reading2 = ReadChannel(2)

	# anti-dither:
	if ((reading2 < reading1 - 6) or (reading2 > reading1 + 6)): # if it's changing
	
	#if reading2 < 650:
		print time.ctime()
		print reading2 		
#		os.popen("sudo shutdown -h now") 	

		reading1 = reading2 
		time.sleep(1)
