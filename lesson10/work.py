import pandas as pd

df = pd.read_csv("sales_transactions_extended.csv", sep = ",", encoding = "utf-8")

print(df)

df = df[(df["Revenue"] > 0) & (df["Cost"] >= 0) & (df["Revenue"] >= df["Cost"] * 0.1)]

print(df)

#task 2.
df["Flag"] = ""


df["Κέρδος"] = df["Revenue"] - df["Cost"]

df["Περιθώριο Κ"] = (df["Κέρδος"] / df["Revenue"]) * 100

print(df)

mask = (df["Περιθώριο Κ"] > 80) | (df["Περιθώριο Κ"] < -20)
mask2 = (df["Περιθώριο Κ"] <= 80) & (df["Περιθώριο Κ"] >= -20)
df.loc[mask, "Flag"] = "Ανώμαλο"
df.loc[mask2, "Flag"] = "Νορμάλ"

print(df)

#task 3.

df["Payment_Status_Value"] = 1
df["Payment_Status_Value"] = df["Payment_Status_Value"].where((df["PaymentStatus"] == "Εκκρεμεί") | (df["PaymentStatus"] == "Καθυστερημένη"), 0)

###########
df["Anomalies_Sum"] = 1
df["Anomalies_Sum"] = df["Anomalies_Sum"].where(df["Flag"] == "Ανώμαλο", 0)

df_customer = df.groupby("CustomerID").agg(
                                          Count = ("CustomerID", "count")
                                        , Revenue = ("Revenue", "sum")
                                        , Cost = ("Cost", "sum")
                                        , Standard_Deviation_Margin = ("Περιθώριο Κ", "std")
                                        , Μέσο_Περιθώριο = ("Περιθώριο Κ", "mean")
                                        , Α_Καθυστερημένων_Εκκρεμών = ("Payment_Status_Value", "sum")
                                        , Α_Ανωμαλιών = ("Anomalies_Sum", "sum"))

df_customer["Ποσοστό_Καθυστερημένων_Εκκρεμών"] = (
    (df_customer["Α_Καθυστερημένων_Εκκρεμών"]  / df_customer["Count"]) * 100)
print(df_customer)

################################################
#Count max period of loses days
max_loses = {}
for customer_id, groups in df.groupby("CustomerID"): # -> 2 apotelesmata 1) Lista ton onomaton ton CustomerId 2) Ola ta groups gia ton kathe pelati
    groups = groups.sort_values("Date")
    counter_days = 0
    max_days = 0
    for kerdos in groups["Κέρδος"]:
        if kerdos < 0:
            counter_days += 1
            max_days = max(max_days, counter_days) #Save the maximum streak
        else:
            counter_days = 0
    max_loses[customer_id] = max_days

print(max_loses)

#Vazoume san stili to dictionary sto report

loss_collumn = pd.Series(max_loses)
df_customer["days_losses"] = loss_collumn
print(df_customer)

#####
df_customer["Σύνθετο Ρίσκο"] = 0

maski = df_customer["Ποσοστό_Καθυστερημένων_Εκκρεμών"] > 25
maskii = df_customer["Μέσο_Περιθώριο"] < 8
maskiii = df_customer["Standard_Deviation_Margin"] > 20
maskiv = df_customer["Revenue"] < 0
maskv = df_customer["Α_Ανωμαλιών"] > 2

#βήμα δεύτερο - loc για να τοποθετηθεί στο ανάλογο κελί
df_customer.loc[maski, "Σύνθετο Ρίσκο"] += 4
df_customer.loc[maskii, "Σύνθετο Ρίσκο"] += 3
df_customer.loc[maskiii, "Σύνθετο Ρίσκο"] += 3
df_customer.loc[maskiv, "Σύνθετο Ρίσκο"] += 6
df_customer.loc[maskv, "Σύνθετο Ρίσκο"] += 5

print(df_customer)

#################
df_customer["Κατηγοριοποίηση Ρίσκου"] = ""
maskvi = (df_customer["Σύνθετο Ρίσκο"] >= 0) & (df_customer["Σύνθετο Ρίσκο"] <= 5)
maskvii = (df_customer["Σύνθετο Ρίσκο"] > 5) & (df_customer["Σύνθετο Ρίσκο"] <= 10)
maskviii = (df_customer["Σύνθετο Ρίσκο"] > 10) & (df_customer["Σύνθετο Ρίσκο"] <= 15)
maskix = df_customer["Σύνθετο Ρίσκο"] >= 16

df_customer.loc[maskvi, "Κατηγοριοποίηση Ρίσκου"] = "Χαμηλό"
df_customer.loc[maskvii, "Κατηγοριοποίηση Ρίσκου"] = "Μεσαίο"
df_customer.loc[maskviii, "Κατηγοριοποίηση Ρίσκου"] = "Υψηλό"
df_customer.loc[maskix, "Κατηγοριοποίηση Ρίσκου"] = "Κρίσιμο"

print(df_customer)

df_customer.to_csv("advanced_customer_risk_report.csv")