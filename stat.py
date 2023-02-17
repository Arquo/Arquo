import pandas as pd
import numpy as np
import matplotlib as plt
from alpha_vantage.timeseries import TimeSeries

api = "B9BL0WND53Q9UY0H"
ts = TimeSeries(api, output_format="pandas")
data, meta = ts.get_weekly("MSFT")
year = 10

close_data =  pd.DataFrame(data.iloc[ :52* year, 3])
percent_change = list(np.log(close_data).diff().iloc[1:,0])
#print(percent_change)
annualized_volatility = np.std(percent_change)*np.sqrt(52)
print(annualized_volatility)

#print(type(annualized_volatility))
#print("Annualized Volatility", annualized_volatility)

annualized_return = pow(close_data.iloc[0,0]/close_data.iloc[-1,0], 1/year)-1
#print("Annualized Return：" , annualized_return)
print("----")
print(data.loc[["2023-02-15","2023-02-10", "2023-02-03"],:])
print("----")
print(data.loc["2023-02-15":"2023-01-06", :])
data = data.sort_index()
print(data.loc["2023-01-06":"2023-02-15", :])