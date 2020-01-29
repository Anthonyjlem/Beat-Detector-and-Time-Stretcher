# Beat Detector and Time Stretcher
This is a Python script that performs beat detection on an audio input and time-stretches an audio output accordingly to match the beats (tempo) detected in real time.
## Notes
There is a short delay in updating the tempo of the audio output, and the script works for audio inputs in the range of 80 to 160 beats per second. Other audio inputs ouside of the range may work if the parameters are changed.

The script can only play .wav files.

The script is currently configured so it plays an audio file in the directory "Music" that is within "Media" that is within the current directory where the script is. If you want to specify a different path, change line 16.
## Dependencies
The script requires the following libraries:
* Aupyom
* Aubio (Requires Microsoft VS and SDK https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk)
* Numpy
* PyAudio

The script works with Python versions 3.5 to 3.7. It may also work with other versions.
