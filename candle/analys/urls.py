from django.contrib import admin
from django.urls import path
from analys import views

urlpatterns = [
    
    path("", views.index, name="home"),
    path('candlestick_list', views.candlestick_list, name='list'),
    path('buy_signal_list', views.buy_signal_list, name='buy_signal')
]