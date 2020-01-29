from aupyom import Sound, Sampler
import aubio # install microsoft VS and SDK https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/
import numpy as np # python has to be at least version 3.5
import os
import pyaudio
import sys

# Initialize pyaudio and sampler
print("Loading...")
sampler = Sampler()
p = pyaudio.PyAudio()

# Initialize the song to be played
song = "hand_in_hand_voice.wav"
tempo = 150 # use tempo of your song here
audio_file = os.path.join(os.path.dirname(__file__), "Media/Music/", song)
audio = Sound.from_file(audio_file)

# Open stream
buffer_size = 1024 # allocate temporary storage of memory to save a few seconds of the stream
pyaudio_format = pyaudio.paFloat32 # makes the format 32 bit floats
n_channels = 1 # number of channels
samplerate = 77175 # number of samples per second inside an audio stream, the higher the more accurate
stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size) # input specifies if this is an input stream

# Setup beat detection
win_s = 4096
hop_s = buffer_size # hop size; how much we can advance the analysis time origin from frame to frame - more overlap will give more analysis points => smoother results across time, but computation is greater
tempo_o = aubio.tempo("default", win_s, hop_s, samplerate)

# Play the song
sampler.play(audio)

print("***Starting***")

while True:
    try:
        # Read stream
        audiobuffer = stream.read(buffer_size)
        signal = np.frombuffer(audiobuffer, dtype=np.float32)
        tempo = tempo_o(signal)
        
        # Update speed at which song is played
        try:
            sfactor = tempo_o.get_bpm()/tempo
            audio.stretch_factor = sfactor
        except ZeroDivisionError:
            sfactor = 1
            audio.stretch_factor = sfactor

        print("Tempo:", tempo_o.get_bpm())
            
    except KeyboardInterrupt:
        break

print("\n***Done Recording***")
stream.stop_stream()
stream.close()
sampler.remove(audio)
p.terminate()
