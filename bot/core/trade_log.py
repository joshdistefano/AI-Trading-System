class TradeLog:
    def __init__(self):
        self.trades = []

    def add_trade(self, entry_price, exit_price, decision):
        profit = exit_price - entry_price

        trade = {
            "entry": entry_price,
            "exit": exit_price,
            "decision": decision,
            "profit": profit
        }

        self.trades.append(trade)

    def show_trades(self):
        for trade in self.trades:
            print(trade)