from alpha_vantage.fundamentaldata import FundamentalData

API = "B9BL0WND53Q9UY0H"

fd = FundamentalData(API, output_format="pandas")

data  = fd.get_cash_flow_annual("MSFT")
print(data)

