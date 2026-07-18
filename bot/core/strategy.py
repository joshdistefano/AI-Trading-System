class Strategy:
    def __init__(self):
        self.name = "Momentum Strategy"
        self.previous_close = None

    def analyze(self, market_data):

        current_close = market_data.close

        if self.previous_close is None:
            self.previous_close = current_close
            return "NO TRADE"

        if current_close > self.previous_close:
            decision = "BUY"

        elif current_close < self.previous_close:
            decision = "SELL"

        else:
            decision = "NO TRADE"

        self.previous_close = current_close

        return decision