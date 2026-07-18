import csv
import os


class TradeJournal:

    def __init__(self, filename="trade_history.csv"):
        self.filename = filename


    def save_trade(self, trade):

        file_exists = os.path.isfile(self.filename)

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Type",
                    "Entry",
                    "Exit",
                    "Result",
                    "Profit"
                ])


            writer.writerow([
                trade["type"],
                trade["entry"],
                trade["exit"],
                trade["result"],
                trade["profit"]
            ])