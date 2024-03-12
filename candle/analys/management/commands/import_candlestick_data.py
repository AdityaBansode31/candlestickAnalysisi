# management/commands/import_candlestick_data.py

import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from analys.models import Candlestick

class Command(BaseCommand):
    help = 'Import candlestick data from a CSV file'

    def handle(self, *args, **kwargs):
        csv_file_path = os.path.join(settings.STATICFILES_DIRS[0], 'candlestick_data.csv')
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            candles = []
            for row in reader:
                timestamp = row['timestamp']
                last_price = float(row['last_price'])

                candle = Candlestick(
                    open_price=last_price,
                    close_price=last_price,
                    high_price=last_price,
                    low_price=last_price,
                    timestamp=timestamp
                )
                candles.append(candle)

            # Bulk create Candlestick objects to improve performance
            Candlestick.objects.bulk_create(candles)

            self.stdout.write(self.style.SUCCESS('Successfully imported candlestick data'))
