class Investor:
    def __init__(self, name):
        self.name = name

    def evaluate(self, stock):
        """Each investor must implement their own evaluation logic."""
        raise NotImplementedError
