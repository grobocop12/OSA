#! /usr/bin/python3
import matplotlib.pyplot as plt, mpld3
from scipy import signal
from scipy.io import wavfile
import scipy
import math
import numpy as np

time = 1

sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')


'''
normalized_samples = np.ndarray(shape= sample_rate*time)
for i in range(sample_rate*time):
    normalized_samples[i] =( (samples[i][0]+samples[i][1])/2)
'''


frequencies, times, spectrogram = signal.spectrogram(samples,
                                                     fs = sample_rate,
                                                     window = signal.hamming(1024),
                                                     scaling = 'spectrum')
'''
frequencies, times, spectrogram = signal.stft(normalized_samples[0:1000], fs = sample_rate, nperseg = 1000)
print(times)

ifft = scipy.fftpack.ifft(samples[0:44101])
'''
print('times',times.shape)
print('frequencies',frequencies.shape)
print('spectrogram',spectrogram.shape)


plt.pcolormesh(times, frequencies, spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.tight_layout()
plt.show()

'''
plt.plot(np.abs(spectrogram))
plt.show()

'''
