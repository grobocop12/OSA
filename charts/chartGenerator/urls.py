from django.urls import path
from . import views

app_name = 'chartGenerator'

urlpatterns = [
    path('', views.index,name = 'index'),
    path('/chart/',views.chart, name= 'chart'),
    ]
