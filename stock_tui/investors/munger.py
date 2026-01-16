# investors/munger.py

from stocks.quantitative import QuantitativeAnalysis

class MungerInvestor:
    @staticmethod
    def check_requirements(ticker_symbol):
        # Fetch stock data using QuantitativeAnalysis
        info = QuantitativeAnalysis.get_data(ticker_symbol)

        # Define criteria based on Munger's investing philosophy
        criteria = {}

        # Munger's criteria thresholds
        criteria['operating_margin'] = QuantitativeAnalysis.check_operating_margin(info)
        criteria['price_to_book'] = QuantitativeAnalysis.check_price_to_book(info)
        criteria['debt_to_equity'] = QuantitativeAnalysis.check_debt_to_equity(info)
        criteria['roe'] = QuantitativeAnalysis.check_roe(info)
        criteria['free_cash_flow'] = QuantitativeAnalysis.check_free_cash_flow(info)

        # Count how many tests pass
        total_passed = sum(1 for passed in criteria.values() if passed)

        # For example, require at least 3 out of 5 tests to pass
        passes = total_passed >= 3

        return passes, criteria
