from core.strategy import Strategy
from core.market_data import MarketData
from core.backtester import Backtester
from core.performance import Performance

print("AI Trading System Started")

strategy = Strategy()

historical_data = [
    MarketData(22000, 1500),
    MarketData(22010, 1600),
    MarketData(21990, 1400),
    MarketData(22030, 1700)
]

backtester = Backtester(strategy)

backtester.run(historical_data)

print("Backtest Results:")

backtester.show_results()

performance = Performance(backtester.results)

performance.analyze()