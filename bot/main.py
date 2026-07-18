import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import config
from strategies.momentum import Strategy
from core.backtester import Backtester
from core.performance import Performance
from core.data_loader import DataLoader
from risk.risk_manager import RiskManager
from trading.trade_manager import TradeManager


print("AI Trading System Started")
print("Market:", config.MARKET)
print("Timeframe:", config.TIMEFRAME)
print("Risk:", config.RISK_PER_TRADE * 100, "%")


risk_manager = RiskManager(
    config.ACCOUNT_SIZE,
    config.RISK_PER_TRADE
)


trade_manager = TradeManager()


risk_amount = risk_manager.calculate_risk_amount()

contracts = risk_manager.calculate_position_size(
    stop_loss_points=50,
    point_value=config.POINT_VALUE
)


print("Risk Amount Per Trade: $", risk_amount)
print("Position Size:", contracts, "contracts")


strategy = Strategy()

loader = DataLoader()

historical_data = loader.load_csv("data/market_data.csv")


backtester = Backtester(strategy)

backtester.run(historical_data)


print("\nBacktest Results:")

backtester.show_results()


performance = Performance(backtester.results)

performance.analyze()


print("\nTrade Simulation:")


trade = trade_manager.open_trade(
    "BUY",
    22000,
    21950,
    22100,
    contracts
)


profit = trade.close_trade(
    22050,
    config.POINT_VALUE
)


print({
    "entry": trade.entry_price,
    "exit": trade.exit_price,
    "profit": profit
})