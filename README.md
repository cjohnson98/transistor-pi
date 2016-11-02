# transistor-pi

Raspberry Pi guts for a transistor radio chassis.

Uses a Raspberry Pi to play audio two ways:

1. Access audio files stored on a USB drive, similar to how a cheap MP3 player works.
2. Access Internet radio streams.

Transistor pi uses potentiometers feeding A to D converters to provide input to the Pi for stream/file selection and volume control, allowing the use of the original volume and tuning knobs on the radio chassis. 

An audio amplifier on the pi output feeds the original radio's internal speaker. The volume control regulates volume on the pi ouptput, so the volume control works for the internal speaker and the headphone jack. Since the original radio had one speaker, the stereo output of the pi is combined for input to the mono amplifier that feeds the speaker. Plugging a stereo headset in disconnects the audio amp and feeds stereo audio to the headset.

A potentiometer replaces the original tuning capacitor. Turning the tuning knob fully counterclockwise sets the tuning pot output to select Internet radio streams. Turning it fully clockwise sets it to select file folders that store MP3 music files. Intermediate points on the tuning dial selects particular streams or music folders.

A usb battery pack (originally intended for use as a cellphone backup battery) provides power. A resistor voltage divider across the power leads feeds another A-D converter, which is read by the pi to determine the battery level. A low battery condition triggers an audio alert and shuts down the pi. The volume control includes an on-off switch, which will also initiate an orderly shutdown when the user turns the unit off. 

Main program file is radio3.py, which starts when the system powers up. 
