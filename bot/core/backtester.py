class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy
        self.results = []

    def run(self, historical_data):
        for data in historical_data:
            decision = self.strategy.analyze(data)

            self.results.append({
                "price": data.price,
                "decision": decision
            })

    def show_results(self):
        for result in self.results:
            print(result)