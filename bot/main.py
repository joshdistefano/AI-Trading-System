from core.strategy import Strategy
from core.market_data import MarketData
from core.trade_log import TradeLog

print("AI Trading System Started")

market = MarketData(22000, 1500)

market.show()

strategy = Strategy()

decision = strategy.analyze(market)

print("Strategy Decision:", decision)

trade_memory = TradeLog()

trade_memory.add_trade({
    "price": market.price,
    "decision": decision
})

print("Trade Memory:")
trade_memory.show_trades()