class RiskManager:

    def __init__(self, account_size, risk_percent):
        self.account_size = account_size
        self.risk_percent = risk_percent

    def calculate_risk_amount(self):

        return self.account_size * self.risk_percent

    def calculate_position_size(self, stop_loss_points, point_value):

        risk_amount = self.calculate_risk_amount()

        if stop_loss_points == 0:
            return 0

        contracts = risk_amount / (stop_loss_points * point_value)

        return int(contracts)