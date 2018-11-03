#! /usr/bin/python3

import scipy.io.wavfile as wavfile
from scipy import signal
import matplotlib.pyplot as plt
import mpld3
import io
import numpy

def plot_chart():
    sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
    #sample_rate, samples = wavfile.read('mono2.wav')
    time = numpy.arange(0,len(samples),dtype = float)
    time = numpy.divide(time, sample_rate)
    fig = plt.figure()
    fig.set_figwidth(12.8)
    fig.set_figheight(7.2)
    plt.plot(time,samples)
    plt.xlabel('Time [s]')
    plt.ylabel('Pressure [Pa]')
    plt.grid()
    plt.tight_layout()
    #plt.axis('off')
    return mpld3.fig_to_html(fig)

def plot_hist():
    sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
    #sample_rate, samples = wavfile.read('mono2.wav')
    hist = numpy.histogram(samples)
    fig = plt.figure()
    plt.hist(samples,density=10,color='g')
    plt.title("To jest kurwa jebany w dupe histogram")
    plt.grid()
    plt.tight_layout()
    #plt.axis('off')
    return mpld3.fig_to_html(fig)



def plot_spect():
    time = 1

    sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
    # sample_rate, samples = wavfile.read('Perturbator.wav')
    normalized_samples = numpy.ndarray(shape=sample_rate * time)
    # for i in range(sample_rate*time):
    #    normalized_samples[i] =( (samples[i][0]+samples[i][1])/2)

    frequencies, times, spectrogram = signal.spectrogram(samples,
                                                         fs=sample_rate,
                                                         window=signal.hamming(256),
                                                         scaling='spectrum')

    # frequencies, times, spectrogram = signal.stft(normalized_samples[0:1000], fs = sample_rate, nperseg = 1000)
    # print(times)

    # ifft = scipy.fftpack.ifft(samples[0:44101]
    fig = plt.figure()
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    return mpld3.fig_to_html(fig)
