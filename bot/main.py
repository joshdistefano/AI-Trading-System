import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import config
from strategies.momentum import Strategy
from core.backtester import Backtester
from core.performance import Performance
from core.data_loader import DataLoader


print("AI Trading System Started")
print("Market:", config.MARKET)
print("Timeframe:", config.TIMEFRAME)
print("Risk:", config.RISK_PER_TRADE * 100, "%")


strategy = Strategy()

loader = DataLoader()

historical_data = loader.load_csv("data/market_data.csv")


backtester = Backtester(strategy)

backtester.run(historical_data)


print("\nBacktest Results:")

backtester.show_results()


performance = Performance(backtester.results)

performance.analyze()