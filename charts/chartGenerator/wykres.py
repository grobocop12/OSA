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
    fig.set_figheight(3.2)
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
    fig.set_figwidth(6.4)
    fig.set_figheight(3.2)
    plt.hist(samples,density=10,color='g')
    plt.title("To jest !@#$% ^&*{} w ~@!# histogram")
    plt.grid()
    plt.tight_layout()
    #plt.axis('off')
    return mpld3.fig_to_html(fig)



def plot_spect():
    fs, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
    NFFT = 1024  # the length of the windowing segments
    time = numpy.arange(0,len(samples),dtype = float)
    time = numpy.divide(time, fs)
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.plot(time, samples)
    Pxx, freqs, bins, im = ax2.specgram(samples, NFFT=NFFT, Fs=fs, noverlap=0)
    # The `specgram` method returns 4 objects. They are:
    # - Pxx: the periodogram
    # - freqs: the frequency vector
    # - bins: the centers of the time bins
    # - im: the matplotlib.image.AxesImage instance representing the data in the plot
    return mpld3.fig_to_html(fig)
