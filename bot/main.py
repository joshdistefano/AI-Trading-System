from core.strategy import Strategy

print("AI Trading System Started")

strategy = Strategy()

decision = strategy.analyze(None)

print("Strategy Decision:", decision)