from trading.trade import Trade


class TradeManager:

    def __init__(self):
        self.trades = []


    def open_trade(self, decision, price, stop_loss, take_profit, contracts):

        trade = Trade(
            decision,
            price,
            stop_loss,
            take_profit,
            contracts
        )

        self.trades.append(trade)

        return trade


    def show_trades(self):

        for trade in self.trades:

            print({
                "type": trade.decision,
                "entry": trade.entry_price,
                "stop": trade.stop_loss,
                "target": trade.take_profit,
                "contracts": trade.contracts
            })