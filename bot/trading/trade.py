class Trade:

    def __init__(self, decision, entry_price, stop_loss, take_profit, contracts):
        self.decision = decision
        self.entry_price = entry_price
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.contracts = contracts
        self.exit_price = None
        self.profit = 0


    def close_trade(self, exit_price, point_value):

        self.exit_price = exit_price

        if self.decision == "BUY":
            points = exit_price - self.entry_price

        elif self.decision == "SELL":
            points = self.entry_price - exit_price

        else:
            points = 0


        self.profit = points * point_value * self.contracts

        return self.profit