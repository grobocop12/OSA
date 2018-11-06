from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import wykres
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Document
from .forms import DocumentForm



def index(request):
    return render(request,'chartGenerator/index.html',{})



def chart(request):
    size = [8.4, 2]
    sample_rate, samples = wykres.load_data()
    signal = wykres.plot_signal(sample_rate,samples,size)
    spect = wykres.plot_spect(sample_rate,samples,size)
    histogram = wykres.plot_hist(sample_rate,samples,size)
    return render(request,'chartGenerator/chart.html',
                  {'signal':signal,'spect':spect, 'histogram': histogram})

def alfa(request):
    return HttpResponse("<b>Oto kurwa nadchodzi zagłada</b>")


def base(request):
    size = [12, 6]
    sample_rate, samples = wykres.load_data()
    spect = wykres.plot_spect(sample_rate,samples,size)
    return render(request,'chartGenerator/spectogram.html',{'spect':spect,})

def test(request):
    size = [12, 6]
    sample_rate, samples = wykres.load_data()
    coś = wykres.test_plot(sample_rate,samples,size)
    return render(request,'chartGenerator/test.html',{'test':coś,})

def upload_file(request):
    if request.method == 'POST':
        form = Document(request.POST, request.FILES)
        if form.is_valid():
            instance = DocumentForm(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = Document()
    return render(request, 'chartGenerator/upload.html', {'form': form})



