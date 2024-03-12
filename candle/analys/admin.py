from django.contrib import admin
from .models import Candlestick, BuySignal

admin.site.register(Candlestick)
admin.site.register(BuySignal)
