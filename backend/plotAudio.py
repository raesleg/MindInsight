# import wave
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import numpy as np
# import io
# import base64

# obj = wave.open('files\TranscribeThis.wav', 'rb')

# sample_freq = obj.getframerate()
# n_samples = obj.getnframes()
# signal_wave = obj.readframes(-1)

# obj.close()

# t_audio = n_samples / sample_freq

# print(t_audio)

# signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# times = np.linspace(0, t_audio, num=n_samples)
# fig = plt.figure(figsize=(15, 5))
# plt.plot(times, signal_array)
# plt.title('Audio Signal')
# plt.ylabel('Signal Wave')
# plt.xlabel('Time (s)')
# plt.xlim(0, t_audio)

# img = io.BytesIO()
# fig.savefig(img, format='png')
# url = base64.b64encode(img.getvalue()).decode()

import os
import wave
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

file_path = 'files/TranscribeThis.wav'

if os.path.exists(file_path):
    obj = wave.open(file_path, 'rb')
    sample_freq = obj.getframerate()
    n_samples = obj.getnframes()
    signal_wave = obj.readframes(-1)
    obj.close()

    t_audio = n_samples / sample_freq
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

else:
    # If the file doesn't exist, provide some default signal
    t_audio = 1.0  # Default duration
    signal_array = np.zeros(44100)  # Placeholder signal
    times = np.linspace(0, t_audio, num=len(signal_array))

    fig = plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.title('Audio Signal (Placeholder)')
    plt.ylabel('Signal Wave')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)

    img = io.BytesIO()
    fig.savefig(img, format='png')
    url = base64.b64encode(img.getvalue()).decode()

# plt.show()  # Display the plot

