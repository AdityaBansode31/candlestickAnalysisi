# management/commands/generate_buy_signals.py

from django.core.management.base import BaseCommand
from analys.models import Candlestick, BuySignal

class Command(BaseCommand):
    help = 'Generate buy signals based on candlestick data'

    def handle(self, *args, **options):
        # Retrieve the candlestick data
        candlesticks = Candlestick.objects.all()

        # Retrieve the open price of the first candlestick
        first_candle = candlesticks.first()
        first_open_price = first_candle.open_price

        # Iterate over the remaining candlesticks
        for candlestick in candlesticks[1:]:
            # Compare the current price with the open price of the first candlestick
            if candlestick.close_price > first_open_price:
                # Generate a buy signal and store it in the BuySignal table
                BuySignal.objects.create(
                    timestamp=candlestick.timestamp,
                    price=candlestick.close_price,
                    signal_type='Buy'
                )

        self.stdout.write(self.style.SUCCESS('Buy signals generated successfully'))
