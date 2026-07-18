import csv
from core.market_data import MarketData


class DataLoader:

    def load_csv(self, filename):

        data = []

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                candle = MarketData(
                    float(row["price"]),
                    float(row["volume"])
                )

                data.append(candle)

        return data