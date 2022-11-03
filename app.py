import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

currency = "USD"
metric = "Close"

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

crypto = ["BTC", "ETH", "XRP", "ADA", "SOL", "DOGE", "MATIC"]
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

combined = combined.pct_change().corr(method = "pearson")

sns.heatmap(combined, annot = True, cmap = "coolwarm")
plt.show()