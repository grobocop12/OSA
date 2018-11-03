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
