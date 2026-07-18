class Strategy:
    def __init__(self):
        self.name = "Momentum Strategy"
        self.previous_price = None

    def analyze(self, market_data):

        if self.previous_price is None:
            self.previous_price = market_data.price
            return "NO TRADE"

        if market_data.price > self.previous_price:
            decision = "BUY"

        elif market_data.price < self.previous_price:
            decision = "SELL"

        else:
            decision = "NO TRADE"

        self.previous_price = market_data.price

        return decision