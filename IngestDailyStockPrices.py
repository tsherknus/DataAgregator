import pandas as pd

ticker = 'TSLA'
path_to_csv = 'DailyStockPriceData/' + ticker + '.csv'

daily_stock_prices = pd.read_csv(path_to_csv, index_col='Date')

print(daily_stock_prices)