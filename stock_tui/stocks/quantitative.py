# stocks/quantitative.py

import yfinance as yf

class QuantitativeAnalysis:
    @staticmethod
    def get_data(ticker_symbol):
        """
        Fetch stock data from Yahoo Finance.
        """
        ticker = yf.Ticker(ticker_symbol)
        return ticker.info

    # Buffett criteria checks
    @staticmethod
    def check_roe(info, min_roe=0.15):
        """
        Check if return on equity (ROE) is ≥ 15%
        """
        roe = info.get('returnOnEquity')
        return roe is not None and roe >= min_roe

    @staticmethod
    def check_debt_to_equity(info, max_debt_to_equity=50):
        """
        Check if debt-to-equity ratio is < 50%
        """
        debt_to_equity = info.get('debtToEquity')
        if debt_to_equity is None:
            return False
        try:
            return float(debt_to_equity) < max_debt_to_equity
        except ValueError:
            return False

    @staticmethod
    def check_profit_margin(info, min_profit_margin=0.1):
        """
        Check if profit margin is ≥ 10%
        """
        profit_margin = info.get('profitMargins')
        return profit_margin is not None and profit_margin >= min_profit_margin

    @staticmethod
    def check_eps_growth(info, min_eps_growth=0.1):
        """
        Check if earnings per share (EPS) growth is ≥ 10%
        """
        eps_growth = info.get('earningsQuarterlyGrowth')
        return eps_growth is not None and eps_growth >= min_eps_growth

    @staticmethod
    def check_forward_pe(info, max_forward_pe=15):
        """
        Check if forward price-to-earnings (PE) ratio is ≤ 15
        """
        forward_pe = info.get('forwardPE')
        return forward_pe is not None and forward_pe <= max_forward_pe

    @staticmethod
    def check_sgr(info, min_sgr=0.10):
        """
        Check if sustainable growth rate (SGR) is ≥ 10%
        """
        roe = info.get('returnOnEquity')
        payout_ratio = info.get('payoutRatio')
        if roe is None or payout_ratio is None:
            return False
        sgr = roe * (1 - payout_ratio)
        return sgr >= min_sgr

    # Munger criteria checks
    @staticmethod
    def check_operating_margin(info, min_operating_margin=0.20):
        """
        Check if operating margin is ≥ 20%
        """
        operating_margin = info.get('operatingMargins')
        return operating_margin >= min_operating_margin if operating_margin is not None else False

    @staticmethod
    def check_price_to_book(info, max_price_to_book=3):
        """
        Check if price-to-book ratio is ≤ 3
        """
        price_to_book = info.get('priceToBook')
        return price_to_book <= max_price_to_book if price_to_book is not None else False

    @staticmethod
    def check_free_cash_flow(info):
        """
        Check if free cash flow is positive
        """
        free_cash_flow = info.get('freeCashflow')
        return free_cash_flow > 0 if free_cash_flow is not None else False
