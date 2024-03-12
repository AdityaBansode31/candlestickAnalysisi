from django.shortcuts import render, HttpResponse
from analys.models import Candlestick, BuySignal


# Create your views here.
def index(request):
    context={
        'variable': 'this is sent,'
    }
    return render(request, 'hello.html', context)

def candlestick_list(request):
    candles = Candlestick.objects.all()
    return render(request, 'candlestick_list.html', {'candles': candles})

def buy_signal_list(request):
    buy_signals = BuySignal.objects.all()
    return render(request, 'buy_signal_list.html', {'buy_signals': buy_signals})