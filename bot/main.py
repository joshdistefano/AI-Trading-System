import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import config
from strategies.momentum import Strategy
from core.data_loader import DataLoader
from risk.risk_manager import RiskManager
from trading.trade_manager import TradeManager
from trading.trade_simulator import TradeSimulator
from trading.trade_performance import TradePerformance


print("AI Trading System Started")
print("Market:", config.MARKET)
print("Timeframe:", config.TIMEFRAME)
print("Risk:", config.RISK_PER_TRADE * 100, "%")


risk_manager = RiskManager(
    config.ACCOUNT_SIZE,
    config.RISK_PER_TRADE
)

trade_manager = TradeManager()

simulator = TradeSimulator(
    config.POINT_VALUE
)

strategy = Strategy()

loader = DataLoader()

historical_data = loader.load_csv("data/market_data.csv")


contracts = risk_manager.calculate_position_size(
    stop_loss_points=50,
    point_value=config.POINT_VALUE
)


trades = []


for candle in historical_data:

    decision = strategy.analyze(candle)

    print(
        "Price:",
        candle.close,
        "Decision:",
        decision
    )


    if decision == "BUY" or decision == "SELL":

        trade = trade_manager.open_trade(
            decision,
            candle.close,
            candle.close - 50 if decision == "BUY" else candle.close + 50,
            candle.close + 100 if decision == "BUY" else candle.close - 100,
            contracts
        )

        trades.append(trade)



results = []


for trade in trades:

    result = simulator.simulate(
        trade,
        historical_data
    )

    results.append(result)


print("\nTrade Results:")

for result in results:
    print(result)


performance = TradePerformance(results)

performance.analyze()