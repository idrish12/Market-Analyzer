import time

from risk_manager import RiskManager

# Simulating execution on historical order block tap

class StrategyTester:

def __init__(self, trading_pair="BTC/USDT"):

self.pair = trading_pair

        self.is_running = False

self.risk_module = RiskManager(1000)

    def load_historical_data(self):

print(f"Fetching order block history for {self.pair}...")

return [63500, 63000, 64200, 62800]

    def run_test(self):
