# transistor-pi

Raspberry Pi guts for a transistor radio chassis.

Uses a Raspberry Pi to play audio two ways:

1. Access audio files stored on a USB drive, similar to how a cheap MP3 player works.
2. Access Internet radio streams.

Uses potentiometers feeding A to D converters to provide input to the Pi for stream/file selection and volume control, allowing the use of the volume and tuning knobs on the original radio chassis. 

An audio amplifier on the pi output feeds the original radio's internal speaker. The volume control regulates volume on the pi ouptput, so the volume control works for the internal speaker and the headphone jack.

A potentiometer replaces the original tuning capacitor. Turning the tuning knob fully counterclockwise sets the tuning pot output to select Internet radio streams. Turning it fully clockwise sets it to select file folders that store MP3 music files.
