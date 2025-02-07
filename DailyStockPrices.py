import yfinance as yf
import pandas as pd
import time

with open('RUT_1000_tickers.txt', 'r') as file:
    for ticker in file:
        ticker = ticker.strip()
        print(ticker)
        path_to_save_csv = 'DailyStockPriceData/' + ticker + '.csv'

        data = yf.download(tickers=ticker, period='max', interval='1d')

        data.columns = data.columns.get_level_values(0)

        data = data.reset_index(drop=False)

        df = pd.DataFrame(columns=['Date', 'Close', 'High', 'Low', 'Open', 'Volume'], index=[])

        data['Close'] = data['Close'].round(2)
        data['High'] = data['High'].round(2)
        data['Low'] = data['Low'].round(2)
        data['Open'] = data['Open'].round(2)

        df['Date'] = data['Date']
        df['Close'] = data['Close']
        df['High'] = data['High']
        df['Low'] = data['Low']
        df['Open'] = data['Open']
        df['Volume'] = data['Volume']

        df.set_index('Date')

        data.to_csv(path_to_save_csv, index=False)

        time.sleep(30)