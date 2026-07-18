def calculate_vwap(prices, volumes):

    total_volume = sum(volumes)

    if total_volume == 0:
        return None

    total_value = 0

    for price, volume in zip(prices, volumes):
        total_value += price * volume

    return total_value / total_volume