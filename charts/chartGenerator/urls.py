from django.urls import path
from . import views

app_name = 'chartGenerator'

urlpatterns = [
    path('', views.index,name = 'index'),
    path('/chart/',views.chart, name= 'chart'),
    path('/alfa/',views.alfa, name= 'alfa'),
    path('/base/',views.base, name= 'base')
    ]
