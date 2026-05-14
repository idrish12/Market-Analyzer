import math

from config import config_data

# Risk Management and Position Sizing Module

class RiskManager:

    def __init__(self, account_balance):

self.balance = account_balance

        self.max_risk_percent = 0.01  # Default 1% risk per trade

def calculate_position_size(self, entry_price, stop_loss):

"""Determines how much to buy based on risk parameters"""

risk_amount = self.balance * self.max_risk_percent

price_risk = abs(entry_price - stop_loss)

if price_risk == 0:

            return 0

        size = risk_amount / price_risk

        return round(size, 4)
