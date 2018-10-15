#! /usr/bin/python3

import scipy.io.wavfile as wavfile
from scipy import signal
import matplotlib.pyplot as plt
import io
import numpy

sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
#sample_rate, samples = wavfile.read('mono2.wav')
time = numpy.arange(0,len(samples),dtype = float)
time = numpy.divide(time, sample_rate)
plt.plot(time,samples)
plt.xlabel('Time [s]')
plt.ylabel('Pressure [Pa]')
plt.grid(animated = True)
plt.show()
