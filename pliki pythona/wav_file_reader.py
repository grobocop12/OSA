#! /usr/bin/python3
import matplotlib.pyplot as plt, mpld3
from scipy import signal
from scipy.io import wavfile
import scipy
import math
import numpy as np

time = 1

sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')




frequencies, times, spectrogram = signal.spectrogram(samples,
                                                     fs = sample_rate,
                                                     window = signal.hamming(1024),
                                                     scaling = 'spectrum')

print('times',times.shape)
print('frequencies',frequencies.shape)
print('spectrogram',spectrogram.shape)


plt.pcolormesh(times, frequencies, spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.tight_layout()
plt.show()

S
