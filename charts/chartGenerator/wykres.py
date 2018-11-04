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

    fig.set_figwidth(12.4)
    fig.set_figheight(12.2)

    ax1.plot(time, samples)  #  pierwsza zmienna




    ax2.specgram(samples, NFFT=NFFT, Fs=fs, noverlap=0) # Druga zmienna






    ax3.hist(samples, density=10, color='g')



    return mpld3.fig_to_html(fig)


def connect_bbox(bbox1, bbox2,
                 loc1a, loc2a, loc1b, loc2b,
                 prop_lines, prop_patches=None):
    if prop_patches is None:
        prop_patches = {
            **prop_lines,
            "alpha": prop_lines.get("alpha", 1) * 0.2,
        }

    c1 = BboxConnector(bbox1, bbox2, loc1=loc1a, loc2=loc2a, **prop_lines)
    c1.set_clip_on(False)
    c2 = BboxConnector(bbox1, bbox2, loc1=loc1b, loc2=loc2b, **prop_lines)
    c2.set_clip_on(False)

    bbox_patch1 = BboxPatch(bbox1, **prop_patches)
    bbox_patch2 = BboxPatch(bbox2, **prop_patches)

    p = BboxConnectorPatch(bbox1, bbox2,
                           # loc1a=3, loc2a=2, loc1b=4, loc2b=1,
                           loc1a=loc1a, loc2a=loc2a, loc1b=loc1b, loc2b=loc2b,
                           **prop_patches)
    p.set_clip_on(False)

    return c1, c2, bbox_patch1, bbox_patch2, p


def zoom_effect01(ax1, ax2, xmin, xmax, **kwargs):
    """
    ax1 : the main axes
    ax1 : the zoomed axes
    (xmin,xmax) : the limits of the colored area in both plot axes.

    connect ax1 & ax2. The x-range of (xmin, xmax) in both axes will
    be marked.  The keywords parameters will be used ti create
    patches.

    """

    trans1 = blended_transform_factory(ax1.transData, ax1.transAxes)
    trans2 = blended_transform_factory(ax2.transData, ax2.transAxes)

    bbox = Bbox.from_extents(xmin, 0, xmax, 1)

    mybbox1 = TransformedBbox(bbox, trans1)
    mybbox2 = TransformedBbox(bbox, trans2)

    prop_patches = {**kwargs, "ec": "none", "alpha": 0.2}

    c1, c2, bbox_patch1, bbox_patch2, p = connect_bbox(
        mybbox1, mybbox2,
        loc1a=3, loc2a=2, loc1b=4, loc2b=1,
        prop_lines=kwargs, prop_patches=prop_patches)

    ax1.add_patch(bbox_patch1)
    ax2.add_patch(bbox_patch2)
    ax2.add_patch(c1)
    ax2.add_patch(c2)
    ax2.add_patch(p)

    return c1, c2, bbox_patch1, bbox_patch2, p


def zoom_effect02(ax1, ax2, **kwargs):
    """
    ax1 : the main axes
    ax1 : the zoomed axes

    Similar to zoom_effect01.  The xmin & xmax will be taken from the
    ax1.viewLim.
    """

    tt = ax1.transScale + (ax1.transLimits + ax2.transAxes)
    trans = blended_transform_factory(ax2.transData, tt)

    mybbox1 = ax1.bbox
    mybbox2 = TransformedBbox(ax1.viewLim, trans)

    prop_patches = {**kwargs, "ec": "none", "alpha": 0.2}

    c1, c2, bbox_patch1, bbox_patch2, p = connect_bbox(
        mybbox1, mybbox2,
        loc1a=3, loc2a=2, loc1b=4, loc2b=1,
        prop_lines=kwargs, prop_patches=prop_patches)

    ax1.add_patch(bbox_patch1)
    ax2.add_patch(bbox_patch2)
    ax2.add_patch(c1)
    ax2.add_patch(c2)
    ax2.add_patch(p)

    return c1, c2, bbox_patch1, bbox_patch2, p


def plot_zoom():
    fs, samples = wavfile.read('Bit - Hacknet OST - 08 You Got Mail.wav')
    NFFT = 1024  # the length of the windowing segments
    time = numpy.arange(0, len(samples), dtype=float)
    time = numpy.divide(time, fs)


    fig = plt.figure(1)
    fig.set_figwidth(6.4)
    fig.set_figheight(3.2)
    ax1 = plt.subplot(221)
    ax2 = plt.subplot(212)
    ax2.specgram(samples, NFFT=NFFT, Fs=fs, noverlap=0)
    ax1.set_xlim(0, 1)
    ax2.set_xlim(0, 5)
    zoom_effect01(ax1, ax2, 0.2, 0.8)


    ax1 = plt.subplot(222)
    ax1.set_xlim(2, 3)
    ax2.set_xlim(0, 5)
    zoom_effect02(ax1, ax2)

    return mpld3.fig_to_html(fig)