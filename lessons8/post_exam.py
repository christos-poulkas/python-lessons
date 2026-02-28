#ερώτηση 12
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("prices_one.csv", sep=",", encoding = "utf-8") #polles fores ta csv den einai komma separated, endexetai na vazoun ellhniko ervthmatiko (;)

print(df.head(10))

#indexes
print(df.index)

print("///////////////")

#collumns
print(df.columns)

print("///////////////")

#values
print(df.values)

print("///////////////")

df_max20 = df[df["Close"] > 0]

print(df_max20)

print("///////////////")

df_new = df_max20["Close"]

df_list = df_new.values
print(df_list)

list_ma5 = [None, None, None, None]

for index, item in enumerate(df_list[4:], start=4): #sthn enumerate to in einai anapodo
    ma5 = (df_list[index] + df_list[index-1] + df_list[index-2] + df_list[index-3] + df_list[index-4]) / 5
    list_ma5.append(ma5)

print(list_ma5)

df_max20["MA5"] = list_ma5

print("///////////////")

print(df_max20)

list_buy = [False, False, False, False, False]

for index, item in enumerate(df_list[5:], start=5): #sthn enumerate to in einai anapodo
    if df_list[index] > list_ma5[index] and df_list[index-1] <= list_ma5[index-1]:
        list_buy.append(True)
    else:
        list_buy.append(False)

print(list_buy)

df_max20["BUY SIGNAL"] = list_buy

print(df_max20)

x_values = df_max20["Date"]
y_values = df_max20["MA5"]

x1_values = df_max20["Date"]
y1_values = df_max20["Close"]

plt.plot(x_values,y_values)
plt.plot(x1_values,y1_values)

plt.show()

df_max20 = df_max20[df_max20["BUY SIGNAL"] == True]

print(df_max20)

df_max20.to_csv("buy_signal.csv")

