import tkinter as tk
import sounddevice as sd
import wavio as wv
from datetime import datetime
root = tk.Tk()
root.title("Audio recorder")

def gui_recorder():
    freq = 44100

    # Recording duration in seconds
    duration = 5

    # Start recording (mono)
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    sd.wait()  # Wait until recording is finished
    filename = datetime.now().strftime("recording_%Y%m%d_%H%M%S.wav")

    # Save as WAV files
    # write("recording0.wav", freq, recording)
    wv.write(filename, recording, freq, sampwidth=2)
    print("recording has been saved")
    root.destroy()
tk.Label(root, text = "Click to record").pack(pady = 10)
tk.Button(root, text = "Record Audio", command = gui_recorder,  bg = "red", fg = "white").pack(pady = 50)
root.mainloop()