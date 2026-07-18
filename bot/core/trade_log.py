class TradeLog:
    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        self.trades.append(trade)

    def show_trades(self):
        for trade in self.trades:
            print(trade)