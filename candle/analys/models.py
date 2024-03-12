from django.db import models

class Candlestick(models.Model):
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()

class BuySignal(models.Model):
    timestamp = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    signal_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.timestamp} - {self.price} ({self.signal_type})'