class TradePerformance:

    def __init__(self, results):
        self.results = results


    def analyze(self):

        wins = 0
        losses = 0
        open_trades = 0

        total_profit = 0

        winning_trades = []
        losing_trades = []


        for trade in self.results:

            profit = trade["profit"]

            if trade["result"] == "OPEN":
                open_trades += 1
                continue


            total_profit += profit


            if trade["result"] == "WIN":

                wins += 1
                winning_trades.append(profit)


            elif trade["result"] == "LOSS":

                losses += 1
                losing_trades.append(profit)


        closed_trades = wins + losses


        win_rate = 0

        if closed_trades > 0:
            win_rate = (wins / closed_trades) * 100


        average_win = 0

        if winning_trades:
            average_win = sum(winning_trades) / len(winning_trades)


        average_loss = 0

        if losing_trades:
            average_loss = sum(losing_trades) / len(losing_trades)


        print("\nTrade Performance")
        print("-----------------")
        print("Closed Trades:", closed_trades)
        print("Wins:", wins)
        print("Losses:", losses)
        print("Open Trades:", open_trades)
        print("Win Rate:", round(win_rate, 2), "%")
        print("Total Profit:", total_profit)
        print("Average Win:", average_win)
        print("Average Loss:", average_loss)