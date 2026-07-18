class Performance:
    def __init__(self, results):
        self.results = results

    def analyze(self):
        total_trades = len(self.results)

        wins = 0
        losses = 0
        total_profit = 0

        for trade in self.results:
            profit = trade["profit"]

            total_profit += profit

            if profit > 0:
                wins += 1

            elif profit < 0:
                losses += 1

        win_rate = 0

        if total_trades > 0:
            win_rate = (wins / total_trades) * 100

        print("Performance Report")
        print("------------------")
        print("Trades:", total_trades)
        print("Wins:", wins)
        print("Losses:", losses)
        print("Win Rate:", round(win_rate, 2), "%")
        print("Total Profit:", total_profit)