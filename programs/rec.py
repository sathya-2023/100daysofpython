import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration in seconds
duration = 5

# Start recording (mono)
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()  # Wait until recording is finished

# Save as WAV files
# write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=2)
