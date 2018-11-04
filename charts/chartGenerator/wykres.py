#! /usr/bin/python3

import scipy.io.wavfile as wavfile
from scipy import signal
import matplotlib.pyplot as plt
import mpld3
import io
import numpy
from matplotlib.transforms import (
    Bbox, TransformedBbox, blended_transform_factory)

from mpl_toolkits.axes_grid1.inset_locator import (
    BboxPatch, BboxConnector, BboxConnectorPatch)

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
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3)  # poszczególne zmienne

    fig.set_figwidth(6.4)
    fig.set_figheight(3.2)

    ax1.plot(time, samples)  #  pierwsza zmienna




    ax2.specgram(samples, NFFT=NFFT, Fs=fs, noverlap=0) # Druga zmienna






    ax3.hist(samples, density=10, color='g')



    return mpld3.fig_to_html(fig)


