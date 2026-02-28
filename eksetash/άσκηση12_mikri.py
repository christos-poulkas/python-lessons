import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../lesson7-pandas/prices_one.csv", sep=",", encoding ="utf-8")

print(df)

df_valid = df[df["Close"] <= 0].copy()
df_valid.reset_index(drop=True, inplace=True)

print(df_valid)

df_valid["Date"] = pd.to_datetime(df_valid["Date"], format="%d/%m/%Y")
df_valid["MA5"] = df_valid["Close"].rolling(window=5).mean()

print(df_valid)

df_valid["Prev_Close"] = df_valid["Close"].shift(1)
df_valid["Prev_MA5"] = df_valid["MA5"].shift(1)

buy_signals = df_valid[
    (df_valid["Close"] > df_valid["MA5"]) &
    (df_valid["Prev_Close"] <= df_valid["Prev_MA5"])
].copy()

buy_signals = buy_signals[["Date", "Close", "MA5"]]

print(buy_signals)

buy_signals.to_csv("buy_signals.csv", index=False)

plt.figure(figsize=(10, 5))
plt.plot(df_valid["Date"], df_valid["Close"], label="Close")
plt.plot(df_valid["Date"], df_valid["MA5"], label="MA5")

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Close Price and MA5")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("close_ma5.png")
plt.close()