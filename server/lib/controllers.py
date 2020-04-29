from lib.models import Corporation, Stock
from sqlalchemy import or_
from datetime import date, timedelta, datetime
from collections import defaultdict
from typing import List, Dict


def get_top_gainers(given_date):
    # Get the stocks that will have the highest percentage increase from the current value
    # Over a period of 1 day, 1 week and 1 month
    # What do we need? The current value of all stocks, and the predicted values of 1 day, 1 week and 1 month
    # Percentage Increase = 100 x (Future Value - Current Value) / Current Value

    def response_format(attribute: str) -> List[Dict]:
        result = []
        stocks.sort(key=lambda s: getattr(s, attribute) - s.closing_value, reverse=True)
        for stock in stocks[:group_size]:
            result.append({
                'corporation': stock.corporation.name,
                'symbol': stock.corporation.symbol,
                'gain': round(100*(getattr(stock, attribute) - stock.closing_value)/stock.closing_value, 2)
            })

        return result

    response, group_size = {}, 5
    given_date = datetime.strptime(given_date, "%d%m%Y").date()
    stocks: List[Stock] = Stock.query.join(Corporation).filter(Stock.record_date == given_date).all()
    response['day'] = response_format('day_prediction_value')
    response['week'] = response_format('week_prediction_value')
    response['month'] = response_format('month_prediction_value')
    return response
