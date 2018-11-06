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

def load_data():
    sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
    return sample_rate , samples

def plot_signal(sample_rate, samples,size):
    [width, height] = size
    time = numpy.arange(0,len(samples),dtype = float)
    time = numpy.divide(time, sample_rate)
    fig = plt.figure()
    fig.set_figwidth(width)
    fig.set_figheight(height)
    f_poly = signal.decimate(samples,20,  ftype='fir')
    time2 = signal.decimate(time, 20)
    plt.plot(time2,f_poly)
    plt.title('Sygnał')
    plt.xlabel('Czas [s]')
    plt.ylabel('Ciśnienie [Pa]')
    plt.grid()
    plt.tight_layout()
    #plt.axis('off')
    return mpld3.fig_to_html(fig)

def plot_hist(sample_rate , samples,size):
    [width, height] = size
    hist = numpy.histogram(samples)
    fig = plt.figure()
    fig.set_figwidth(width)
    fig.set_figheight(height)
    plt.hist(samples,70,density=5,color='g')
    plt.title('Histogram')
    plt.grid()
    plt.tight_layout()
    #plt.axis('off')
    return mpld3.fig_to_html(fig)



def plot_spect(sample_rate , samples,size):
    [width, height] = size
    NFFT = 1024  # the length of the windowing segments
    time = numpy.arange(0,len(samples),dtype = float)
    time = numpy.divide(time, sample_rate)

    fig = plt.figure()
    fig.set_figwidth(width)
    fig.set_figheight(height)
    plt.specgram(samples, NFFT=NFFT, Fs=sample_rate, noverlap=0) # Druga zmienna
    plt.title('Spektrogram')
    plt.ylabel('Częstotliwość [Hz]')
    plt.xlabel('Czas [s]')
    plt.grid()
    plt.tight_layout()
    return mpld3.fig_to_html(fig)


def test_plot(sample_rate , samples,size):
    [width, height] = size
    NFFT = 1024  # the length of the windowing segments
    time = numpy.arange(0, len(samples), dtype=float)
    time = numpy.divide(time, sample_rate)
    f_poly = signal.decimate(samples, 20, ftype='fir')
    time2 = signal.decimate(time, 20)

    fig = plt.figure()



    t = numpy.arange(0, 10, 0.01)

    ax1 = plt.subplot(211)
    ax1.plot(time2, f_poly)

    ax2 = plt.subplot(212, sharex=ax1)
    ax2.specgram(samples, NFFT=NFFT, Fs=sample_rate, noverlap=0)  # Druga zmienna
    return mpld3.fig_to_html(fig)
