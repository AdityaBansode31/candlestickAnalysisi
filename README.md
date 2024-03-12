# candlestickAnalysisi

code is present in the master branch

 I have imported the CSV file data into our Django project and displayed it in the required table format. Additionally, I have implemented the logic to generate buy signals based on the specified criteria and stored them in the database.


# HOME PAGE
![Screenshot 2024-03-12 134127](https://github.com/AdityaBansode31/candlestickAnalysisi/assets/79712975/bdbb2b00-0a4a-4b9b-98bb-87a0e7b47984)

# CANDLESTICK DATA LIST
![Screenshot 2024-03-12 134152](https://github.com/AdityaBansode31/candlestickAnalysisi/assets/79712975/a5d0bc2f-021b-4a9a-8152-e242b9902ac6)

# BUYING SIGNAL LIST
![Screenshot 2024-03-12 134208](https://github.com/AdityaBansode31/candlestickAnalysisi/assets/79712975/7831aa68-d331-48be-84ee-e008eec6a3aa)

# EXPLINATION
yaml code
candlesticks:
  - timestamp: "2024-02-23 09:17:29"  open: 235.0  close: 236.0
  - timestamp: "2024-02-23 09:17:30"  open: 234.6  close: 234.8
  - timestamp: "2024-02-23 09:17:31"  open: 234.85  close: 235.6
  - timestamp: "2024-02-23 09:17:32"  open: 235.6  close: 236.2
  - timestamp: "2024-02-23 09:17:33"  open: 235.95  close: 235.9

Now, let's walk through the steps to generate buy signals using this YAML representation of your data:

1. Define the Conditions: We'll use the condition that a buy signal is triggered when the close price of a candlestick is at least 1% higher than the open price.

2. Calculate Candlestick Metrics: We'll iterate through the candlestick data and compare the close price with the open price of the previous candlestick.

3. Iterate Through Candlesticks: Starting from the second candlestick, we'll loop through each candlestick in the list.

4. Compare Prices: For each candlestick, we'll compare the close price with the open price of the previous candlestick.

5. Generate Buy Signal: If the close price is at least 1% higher than the open price, we'll trigger a buy signal for that candlestick.

6. Record Buy Signals: We'll record the timestamp and price of the candlestick where the buy signal occurred.

7. Display Buy Signals: Once all buy signals have been generated, we'll display them in a user-friendly format.

# ADMIN PAGE SQLITE MODELS
![Screenshot 2024-03-12 134247](https://github.com/AdityaBansode31/candlestickAnalysisi/assets/79712975/7080fc76-e4c9-4cce-a9df-95644c5c5079)
