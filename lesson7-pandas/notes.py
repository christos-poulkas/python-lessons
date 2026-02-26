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

data = {
    "Company": ["Amazon","Tesla","Apple","Samsung"],
    "Profit": [57,21,7,23],
    "NumEmployers": [12,23,34,12]
}

df  = pd.DataFrame(data)

print(df[df["NumEmployers"] > 20])

print(df[df["Company"].str.contains("Samsung")]) # Einai to idio df["Company] == "Samsung"
print(df[df["Company"].str.upper().str.startswith("A")])


df = df.sort_values("Company",ascending = True)

print(df)

#Group By

data = {
    "Company": ["Amazon","Amazon","Apple","Amazon"],
    "Profit": [57,21,7,23],
    "NumEmployers": [12,23,34,12]
}

df  = pd.DataFrame(data)

df = df.groupby("Company").sum()

print(df)