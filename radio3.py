#!/usr/bin/python
# selects stream from tuning dial position
# monitors battery condition

from __future__ import division
import spidev
import time
import os
import gc
import sys
import math

global tune1, tune2, tunerout, volts2, volume1, volume2, volumeout, IStream
tune1 = False
tune2 = False
tunerout = False
volts2 = False
volume1 = False
volume2 = False
volumeout = False
IStream = False  # start system on mp3s

# open spi port:
spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):  # read channel from mcd3008; channel must be integer 0 - 7
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data # returns value between 0 and 1023

# check volume control here. If < 1,
	# set voice control

os.popen("mpc repeat on") # playlist will loop
os.popen("mpc play -q ")  # start playing whatever the last playlist was

while True:  # main loop

	# Check battery:
	volts2 = ReadChannel(2)
	if ((volts2 < 210) and (volts2 > 10)): # battery is present, but weak
		print time.ctime()
		print volts2
		os.popen("mpc clear -q ")
		os.popen("espeak -a 150 'battery low' 2>/dev/null")
		os.popen("sudo shutdown -h now") # shutdown on low battery
		time.sleep(1)
		sys.exit()

	# read the tuning dial:
	tune2 = ReadChannel(0)

	if (tune2 == 0):
		IStream = False
	if (tune2 == 1023):
		IStream = True

	ditherfactor = int(tune2 / 50) + 3 # anti-dither
	if ((tune2 < tune1 - ditherfactor) or (tune2 > tune1 + ditherfactor)): # tuning change?
		tunerout = int(tune2 / 25) # returns a value of 0 to 40
		tunerout = tunerout + (100 * IStream)  # adds 100 to base if playing streams
		tuneroutstring = "mpc load -q " + str(tunerout) # set up the mpc instruction
		os.popen("mpc clear -q") # stop play and clear the playlist
		os.popen(tuneroutstring) # load the new playlist
		os.popen("mpc play -q ") # start play

		tune1 = tune2 
		time.sleep(.5)

	# read the volume control:
	volume2 = ReadChannel(1)
	ditherfactor = int(volume2 / 50) + 1
	if ((volume2 < volume1 - ditherfactor) or (volume2 > volume1 + ditherfactor)):
		volumeout = int(math.log((volume2 + 1),10) * 33) + 1  # VC smoothing
		volumeoutstring = "mpc volume -q " + str(volumeout)
		os.popen(volumeoutstring)
		volume1 = volume2
		time.sleep(.5)
