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
import wave
import struct
import os
import base64
import django.core.files
import mimetypes
from django.core.files.base import ContentFile
import uuid


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
    cos = wykres.test_plot(sample_rate,samples,size)
    return render(request,'chartGenerator/test.html',{'test':cos,})

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
        start = float(request.GET.get('start'))
        stop = float(request.GET.get('stop'))
        
        if start < stop:
            t = start
            start = stop
            stop = t
        
        sample_rate = request.session['sample_rate']
        samples = np.asanyarray(request.session['samples'])
        dT = 1/sample_rate
        time = np.arange(0,len(samples),dtype = float)
        time = np.multiply(time,dT)
        
        first = np.where(time>start)[0][0]
        last = np.where(time<stop)[-1][-1]
        samples = samples[first:last]
        
        file_name =  str(uuid.uuid4())+'.wav'
        file_full_path = "tempfiles/{0}".format(file_name)
        fout = wave.open(file_full_path,'wb')
        fout.setnchannels(1)
        fout.setsampwidth(2)
        fout.setframerate(sample_rate)
        fout.setcomptype('NONE','Not Compressed')
        BinStr=b''
        for i in range(len(samples)):
            BinStr = BinStr + struct.pack('h',samples[i])
        fout.writeframesraw(BinStr)
        fout.close()
        
        #string_to_return = get_the_string() # get the string you want to return.
        file_to_send = ContentFile(file_name)
        
        
        
        with open(file_full_path,'rb') as f:
            data = f.read()
        
        
        response = HttpResponse(data, content_type=mimetypes.guess_type(file_full_path)[0])
        response['Content-Disposition'] = "attachment; filename={0}".format(file_name)
        response['Content-Length'] = os.path.getsize(file_full_path)
        response.streaming = True
        os.remove(file_full_path)
        return response
    
        
        
    return render(request, 'chartGenerator/download.html')
    

def poligon(request,sample_rate,samples):
    size = (16, 8)
    signal, time = wykres.poligon(sample_rate,samples)
    #request.session['time'] = time.tolist()
    spect, frequencies ,times = wykres.spectimg(sample_rate,samples)
    return render(request,'chartGenerator/poligon.html',{'rawData':json.dumps(samples.tolist()),'time':json.dumps(time.tolist()),'signal':json.dumps(signal.tolist()),'spect':json.dumps(spect.tolist()),'fq':json.dumps(frequencies.tolist()),'t':json.dumps(times.tolist())})
    

