def calculate_ema(prices, period):

    if len(prices) < period:
        return None

    multiplier = 2 / (period + 1)

    ema = prices[0]

    for price in prices[1:]:
        ema = (price - ema) * multiplier + ema

    return ema