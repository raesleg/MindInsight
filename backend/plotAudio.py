import wave
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import io
import base64

obj = wave.open('TranscribeThis.wav', 'rb')

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, num=n_samples)
fig = plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio Signal')
plt.ylabel('Signal Wave')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)

img = io.BytesIO()
fig.savefig(img, format='png')
url = base64.b64encode(img.getvalue()).decode()

