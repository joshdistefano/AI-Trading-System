from core import config
from core.strategy import Strategy
from core.backtester import Backtester
from core.performance import Performance
from core.data_loader import DataLoader

print("AI Trading System Started")
print("Market:", config.MARKET)
print("Timeframe:", config.TIMEFRAME)
print("Risk:", config.RISK_PER_TRADE * 100, "%")

strategy = Strategy()

loader = DataLoader()

historical_data = loader.load_csv("market_data.csv")

backtester = Backtester(strategy)

backtester.run(historical_data)

print("\nBacktest Results:")

backtester.show_results()

performance = Performance(backtester.results)

performance.analyze()