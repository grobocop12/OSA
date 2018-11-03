from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import wykres

# Create your views here.

def index(request):
    return render(request,'chartGenerator/index.html',{})



def chart(request):
    html = wykres.plot_chart()
    return render(request,'chartGenerator/chart.html',{'chart_figure':html,})

def alfa(request):
    return HttpResponse("<b>Oto kurwa nadchodzi zagłada</b>")

def base(request):
    html = wykres.plot_hist()
    return render(request,'chartGenerator/chart.html',{'chart_figure':html,})
