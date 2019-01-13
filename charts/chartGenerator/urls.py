from django.urls import path
from . import views

app_name = 'chartGenerator'

urlpatterns = [
    path('', views.index,name = 'index'),
    path('chart/',views.chart, name= 'chart'),
    path('alfa/',views.alfa, name= 'alfa'),
    path('base/',views.base, name= 'base'),
    path('test/',views.test,name = 'test'),
    path('poligon/',views.poligon,name = 'poligon'),
    path('upload/',views.upload_file, name='upload'),
    path('download/',views.download_file, name='download')
    ]
