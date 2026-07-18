class Performance:

    def __init__(self, results):
        self.results = results

    def analyze(self):

        trades = [
            result for result in self.results
            if result["decision"] != "NO TRADE"
        ]

        wins = 0
        losses = 0
        total_profit = 0

        for trade in trades:

            total_profit += trade["profit"]

            if trade["profit"] > 0:
                wins += 1

            elif trade["profit"] < 0:
                losses += 1

        win_rate = 0

        if len(trades) > 0:
            win_rate = (wins / len(trades)) * 100

        print("Performance Report")
        print("------------------")
        print("Trades:", len(trades))
        print("Wins:", wins)
        print("Losses:", losses)
        print("Win Rate:", round(win_rate, 2), "%")
        print("Total Profit:", total_profit)