from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import wykres

# Create your views here.

def index(request):
    return render(request,'chartGenerator/index.html',{})



def chart(request):
    sample_rate, samples = wykres.load_data()
    signal = wykres.plot_signal(sample_rate,samples)
    spect = wykres.plot_spect(sample_rate,samples)
    histogram = wykres.plot_hist(sample_rate,samples)
    return render(request,'chartGenerator/chart.html',
                  {'signal':signal,'spect':spect, 'histogram': histogram})

def alfa(request):
    return HttpResponse("<b>Oto kurwa nadchodzi zagłada</b>")


def base(request):
    sample_rate, samples = wykres.load_data()
    spect = wykres.plot_spect(sample_rate,samples)
    return render(request,'chartGenerator/chart.html',{'spect':spect,})

