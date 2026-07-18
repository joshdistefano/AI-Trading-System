class MarketData:
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume

    def show(self):
        print("Current Price:", self.price)
        print("Volume:", self.volume)