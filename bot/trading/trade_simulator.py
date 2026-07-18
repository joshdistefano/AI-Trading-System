class TradeSimulator:

    def __init__(self, point_value):
        self.point_value = point_value


    def simulate(self, trade, candles):

        start_index = 0

        for i, candle in enumerate(candles):

            if candle.close == trade.entry_price:
                start_index = i
                break


        future_candles = candles[start_index + 1:]


        for candle in future_candles:

            if trade.decision == "BUY":

                if candle.low <= trade.stop_loss:
                    return self.close_trade(
                        trade,
                        trade.stop_loss,
                        "LOSS"
                    )

                if candle.high >= trade.take_profit:
                    return self.close_trade(
                        trade,
                        trade.take_profit,
                        "WIN"
                    )


            elif trade.decision == "SELL":

                if candle.high >= trade.stop_loss:
                    return self.close_trade(
                        trade,
                        trade.stop_loss,
                        "LOSS"
                    )

                if candle.low <= trade.take_profit:
                    return self.close_trade(
                        trade,
                        trade.take_profit,
                        "WIN"
                    )


        return self.close_trade(
            trade,
            candles[-1].close,
            "OPEN"
        )


    def close_trade(self, trade, exit_price, result):

        profit = trade.close_trade(
            exit_price,
            self.point_value
        )

        return {
            "type": trade.decision,
            "entry": trade.entry_price,
            "exit": exit_price,
            "result": result,
            "profit": profit
        }