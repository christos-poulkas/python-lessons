import pandas as pd

data = {
    "Company": ["Apple","Amazon","Tesla"],
    "Profit": [57,21,7],
    "NumEmployers": [12,23,34]
}

df  = pd.DataFrame(data)

print(df)

#Collumns

print(df.columns)

#Values -> Matrix (px 3x2)

print(df.values)

#Indexes (like excel number order)

print(df.index)

zitoumenes_stiles = ["Company","NumEmployers"]

df2 = df[zitoumenes_stiles]

print(df2)

#Head (sou typonei ta prota 5)

print(df.head(2)) # allios df.head() -> 5 prota by default

#Tail (sou typonei ta 5 teleutaia)
print(df.tail(1))

new_df = pd.read_csv("dailyprices.csv",sep=",",encoding = "utf-8")
#pd.read_excel("Reports.xlsx")
print(new_df.head())

data = {
    "Company": ["Apple","Amazon","Tesla"],
    "Profit": [57,21,7],
    "NumEmployers": [12,23,34]
}

df  = pd.DataFrame(data)

df["NetProfit"] = df["Profit"] * 0.21

print(df)

df["misthos"] = df["NumEmployers"] * df["Profit"] * 0.011

print(df)

df.to_csv("out.csv")
df.to_excel("report.xlsx")