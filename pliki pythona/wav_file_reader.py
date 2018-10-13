#! /usr/bin/python3
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import scipy
import math
import numpy as np


sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
ifft = scipy.fftpack.ifft(samples[0:44101])
print(type(ifft))
plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
'''
plt.plot(np.abs(ifft))
plt.show()
'''
