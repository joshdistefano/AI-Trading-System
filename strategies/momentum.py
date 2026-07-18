from indicators.ema import calculate_ema
from indicators.vwap import calculate_vwap


class Strategy:

    def __init__(self):
        self.name = "EMA VWAP Momentum Strategy"
        self.prices = []
        self.volumes = []

    def analyze(self, market_data):

        self.prices.append(market_data.close)
        self.volumes.append(market_data.volume)

        if len(self.prices) < 3:
            return "NO TRADE"

        ema = calculate_ema(self.prices, 3)
        vwap = calculate_vwap(self.prices, self.volumes)

        if market_data.close > ema and market_data.close > vwap:
            return "BUY"

        elif market_data.close < ema and market_data.close < vwap:
            return "SELL"

        else:
            return "NO TRADE"