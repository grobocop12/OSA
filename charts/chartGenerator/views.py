from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import wykres
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
import json
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import TemplateView
import numpy as np
import scipy.io.wavfile as wavfile
import io


def index(request):
    return render(request,'chartGenerator/index.html',{})



def chart(request):
    size = (8.4, 2)
    sample_rate, samples = wykres.load_data()
    signal = wykres.plot_signal(sample_rate,samples,size)
    spect = wykres.plot_spect(sample_rate,samples,size)
    histogram = wykres.plot_hist(sample_rate,samples,size)
    return render(request,'chartGenerator/chart.html',
                  {'signal':signal,'spect':spect, 'histogram': histogram})

def alfa(request):
    return HttpResponse("<b>Oto kurwa nadchodzi zagłada</b>")


def base(request):
    size = (12, 6)
    sample_rate, samples = wykres.load_data()
    spect = wykres.plot_spect(sample_rate,samples,size)
    return render(request,'chartGenerator/spectogram.html',{'spect':spect,})

def test(request):
    size = (12, 6)
    sample_rate, samples = wykres.load_data()
    coś = wykres.test_plot(sample_rate,samples,size)
    return render(request,'chartGenerator/test.html',{'test':coś,})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            sample_rate, samples = wykres.handle_uploaded_file(request.FILES['file'])
            request.session['sample_rate'] = sample_rate
            request.session['samples'] = samples.tolist()
            
            return poligon(request,sample_rate,samples)
    else:
        form = UploadFileForm()
    return render(request, 'chartGenerator/upload.html', {'form': form})

@csrf_exempt
def download_file(request):
    if request.method == 'GET':
        #print('GET REQUEST!!!')
        start = float(request.GET.get('start'))
        stop = float(request.GET.get('stop'))
        sample_rate = request.session['sample_rate']
        samples = np.asanyarray(request.session['samples'])
        T = len(samples)/sample_rate
        print(T)
        dT = T/len(samples)
        
        #time = np.asanyarray(request.session['time'])
        time = np.arange(0,len(samples),dtype = float)
        time = np.multiply(time,dT)
        
        first = np.where(time>start)[0][0]
        last = np.where(time<stop)[-1][-1]
        samples = samples[first:last]
        print(samples)
        wavfile.write('tempfiles/temp.wav', sample_rate, samples)        
        
        
    return render(request, 'chartGenerator/download.html')
    

def poligon(request,sample_rate,samples):
    size = (16, 8)
    signal, time = wykres.poligon(sample_rate,samples)
    #request.session['time'] = time.tolist()
    spect, frequencies ,times = wykres.spectimg(sample_rate,samples)
    return render(request,'chartGenerator/poligon.html',{'rawData':json.dumps(samples.tolist()),'time':json.dumps(time.tolist()),'signal':json.dumps(signal.tolist()),'spect':json.dumps(spect.tolist()),'fq':json.dumps(frequencies.tolist()),'t':json.dumps(times.tolist())})
    

