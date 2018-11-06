#! /usr/bin/python3

import scipy.io.wavfile as wavfile
from scipy import signal
import matplotlib.pyplot as plt
import mpld3
import io
import numpy as np
import pandas as pd
import mpld3.plugins as plugins
from matplotlib.transforms import (
    Bbox, TransformedBbox, blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (
    BboxPatch, BboxConnector, BboxConnectorPatch)

class HelloWorld(plugins.PluginBase):  # inherit from PluginBase
    """Hello World plugin"""
    
    JAVASCRIPT = """
    mpld3.register_plugin("helloworld", HelloWorld);
    HelloWorld.prototype = Object.create(mpld3.Plugin.prototype);
    HelloWorld.prototype.constructor = HelloWorld;
    function HelloWorld(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };
    
    HelloWorld.prototype.draw = function(){
        this.fig.canvas.append("text")
            .text("hello world")
            .style("font-size", 72)
            .style("opacity", 0.3)
            .style("text-anchor", "middle")
            .attr("x", this.fig.width / 2)
            .attr("y", this.fig.height / 2)
    }
    """
    def __init__(self):
        self.dict_ = {"type": "helloworld"}
        


def dummy_data(N,fs):
    x = np.arange(N)
    dT = 1/fs
    x = np.multiply(x,dT)
    y = np.sin(x*2*np.pi*20) - 0.1*np.sin(x*2*np.pi*40)
    return fs, y

def load_data():
    sample_rate, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
    #sample_rate, samples = wavfile.read('mono2.wav')
    #sample_rate, samples = dummy_data(10000,128)
    return sample_rate , samples

def plot_signal(sample_rate, samples,size):
    [width, height] = size
    N = len(samples)
    fig = plt.figure()
    fig.set_figwidth(width)
    fig.set_figheight(height)

    samples = signal.decimate(samples,300,  ftype='fir')
    T = N/sample_rate
    dT = T/len(samples)
    time = np.arange(0,len(samples),dtype = float)
    time = np.multiply(time,dT)
    #labels = ["Point {0}".format(i) for i in range(len(samples))]
    #tooltip = plugins.PointLabelTooltip(samples)

    plt.plot(time,samples)
    plt.title('Sygnał')
    plt.xlabel('Czas [s]')
    plt.ylabel('Ciśnienie [Pa]')
    plt.grid()
    plt.tight_layout()
    #plugins.connect(fig, plugins.PointHTMLTooltip(samples))
    plugins.connect(fig,plugins.MousePosition())
    return mpld3.fig_to_html(fig,template_type="general")

def plot_hist(sample_rate , samples,size):
    [width, height] = size
    hist = np.histogram(samples)
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
    NFFT = 256  # the length of the windowing segments
    time = np.arange(0,len(samples),dtype = float)
    time = np.divide(time, sample_rate)
    

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
    time = np.arange(0, len(samples), dtype=float)
    time = np.divide(time, sample_rate)
    f_poly = signal.decimate(samples, 20, ftype='fir')
    time2 = signal.decimate(time, 20)

    fig = plt.figure()



    t = np.arange(0, 10, 0.01)

    ax1 = plt.subplot(211)
    ax1.plot(time2, f_poly)

    ax2 = plt.subplot(212, sharex=ax1)
    ax2.specgram(samples, NFFT=NFFT, Fs=sample_rate, noverlap=0)  # Druga zmienna
    return mpld3.fig_to_html(fig)

def poligon():
    

    # Define some CSS to control our custom labels
    css = """
    table
    {
      border-collapse: collapse;
    }
    th
    {
      color: #ffffff;
      background-color: #000000;
    }
    td
    {
      background-color: #cccccc;
    }
    table, th, td
    {
      font-family:Arial, Helvetica, sans-serif;
      border: 1px solid black;
      text-align: right;
    }
    """

    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3)

    N = 50
    df = pd.DataFrame(index=range(N))
    df['x'] = np.random.randn(N)
    df['y'] = np.random.randn(N)
    df['z'] = np.random.randn(N)

    labels = []
    for i in range(N):
        label = df.ix[[i], :].T
        label.columns = ['Row {0}'.format(i)]
        # .to_html() is unicode; so make leading 'u' go away with str()
        labels.append(str(label.to_html()))

    points = ax.plot(df.x, df.y, 'o', color='b',
                     mec='k', ms=15, mew=1, alpha=.6)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('HTML tooltips', size=20)

    tooltip = plugins.PointHTMLTooltip(points[0], labels,
                                       voffset=10, hoffset=10, css=css)
    plugins.connect(fig, tooltip)

    return mpld3.fig_to_html(fig)

