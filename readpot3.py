#!/usr/bin/python
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

#def bitstring(n): # from old mcp3002 code
#	s = bin(n)[2:]
#	return '0'*(8-len(s)) + s

def ReadChannel(channel):    # read data from mcp2008; channel must be integer 0 - 7
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data 


while True:  # always loop

	reading2 = ReadChannel(1)

	if (reading2 <> reading1):
		print reading2
		reading1 = reading2 
		time.sleep(1)
