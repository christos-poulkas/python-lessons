import pandas as pd

new_df = pd.read_csv("dailyprices.csv",sep=",",encoding = "utf-8")

ext1 = ["Date", "AAPL"]
APPL = new_df[ext1]
print (new_df.head())
print(APPL.head(7))

APPL["Euros"] = APPL["AAPL"] * 0.85
print(APPL.head(2))

APPL["Price100"] = APPL["AAPL"] * 100

APPL["Valuation"] = APPL["Price100"] > 150

print(APPL.tail(5))

APPL.to_csv("my.csv")
