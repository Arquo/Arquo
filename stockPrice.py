
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from alpha_vantage.timeseries import TimeSeries
API = "B9BL0WND53Q9UY0H"
ts = TimeSeries(API, output_format="pandas")
data, meta= ts.get_intraday(symbol= "MSFT", interval= "1min", outputsize ="full" )
data2 = pd.DataFrame(data)

print(data)

#i = 1
#while i ==1:
  #  data, meta= ts.get_intraday(symbol= "MSFT", interval= "1min", outputsize ="full" )
   # data.to_excel("output.xlsx")
  #  time.sleep(60)

#print(data.loc["2023-02-14"])
#print(data2.loc["2023-02-14"])
#data2.round(2).to_csv("MSFTintraday.csv", index=False, sep="\t")
#plt.plot(data["4. close"], "r--")
#plt.xlabel("Date")
#plt.ylabel("Price")
#plt.show()
