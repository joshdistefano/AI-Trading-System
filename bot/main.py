from core.strategy import Strategy
from core.market_data import MarketData

print("AI Trading System Started")

market = MarketData(22000, 1500)

market.show()

strategy = Strategy()

decision = strategy.analyze(market)

print("Strategy Decision:", decision)