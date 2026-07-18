class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy
        self.results = []

    def run(self, historical_data):
        for i in range(len(historical_data) - 1):

            current = historical_data[i]
            future = historical_data[i + 1]

            decision = self.strategy.analyze(current)

            profit = 0

            if decision == "BUY":
                profit = future.close - current.close

            elif decision == "SELL":
                profit = current.close - future.close

            self.results.append({
                "close": current.close,
                "decision": decision,
                "profit": profit
            })

    def show_results(self):
        for result in self.results:
            print(result)