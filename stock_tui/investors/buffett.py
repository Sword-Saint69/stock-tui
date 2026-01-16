from stocks.quantitative import QuantitativeAnalysis

class BuffettInvestor:
    @staticmethod
    def check_requirements(ticker_symbol):
        # Fetch stock data
        info = QuantitativeAnalysis.get_data(ticker_symbol)

        # Define criteria using quantitative analysis methods
        criteria = {}

        # Buffett's criteria thresholds
        criteria['roe'] = QuantitativeAnalysis.check_roe(info) if info.get('returnOnEquity') is not None else False
        criteria['debt_to_equity'] = QuantitativeAnalysis.check_debt_to_equity(info) if info.get('debtToEquity') is not None else False
        criteria['profit_margin'] = QuantitativeAnalysis.check_profit_margin(info) if info.get('profitMargins') is not None else False
        criteria['eps_growth'] = QuantitativeAnalysis.check_eps_growth(info) if info.get('earningsQuarterlyGrowth') is not None else False
        criteria['forward_pe'] = QuantitativeAnalysis.check_forward_pe(info) if info.get('forwardPE') is not None else False
        criteria['sgr'] = QuantitativeAnalysis.check_sgr(info) if info.get('payoutRatio') is not None and info.get('returnOnEquity') is not None else False

        # Count how many criteria passed
        total_passed = sum(1 for v in criteria.values() if v)

        # The company passes if at least 4 of 6 criteria are met
        passes = total_passed >= 4

        return passes, criteria
