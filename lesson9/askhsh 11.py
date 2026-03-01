import pandas as pd
#1st
df = pd.read_csv("sales_transactions.csv",sep=",",encoding = "utf-8")
df_actual = df[(df["Έσοδα"] > 0) & (df["Κόστος"] >= 0)]
#
print(df.head(10))
print(df.columns)
print(df_actual.head(10))

#2nd
df_actual["Κέρδος"] = df_actual["Έσοδα"] - df_actual["Κόστος"]
df_actual["Περιθώριο Κέρδους"] = (df_actual["Κέρδος"] / df_actual["Έσοδα"]) * 100
print(df_actual)
#

df_actual["Εκκρεμή_Έσοδα"] = df_actual["Έσοδα"].where( df_actual["ΚατάστασηΠληρωμής"] == "Εκκρεμεί", 0)

#3rd
report = df_actual.groupby("Πελάτης").agg(Count = ("Πελάτης", "count"), Συνολικά_Έσοδα = ("Έσοδα", "sum")
                                        , Συνολικό_Κόστος = ("Κόστος", "sum")
                                        , Συνολικό_Κέρδος = ("Κέρδος", "sum")
                                        , Μέσο_Περιθώριο_Κέρδους = ("Περιθώριο Κέρδους", "mean")
                                        , Εκκρεμή_Έσοδα = ("Εκκρεμή_Έσοδα", "sum") )

print(report)

#4th
report["Ρίσκο"] = 0

mask = report["Εκκρεμή_Έσοδα"] > report["Συνολικά_Έσοδα"] * 0.3
mask2 = report["Μέσο_Περιθώριο_Κέρδους"] / 100 < 0.1
mask3 = report["Συνολικό_Κέρδος"] < 0
report.loc[mask, "Ρίσκο"] += 5
report.loc[mask2, "Ρίσκο"] += 3
report.loc[mask3, "Ρίσκο"] += 5
print(report)

#5 βήμα πρώτο - δημιουργία μάσκας για true-false conditions
report["Αξιολόγηση Ρίσκου"] = ""

maski = report["Ρίσκο"] < 5
maskii = (report["Ρίσκο"] >= 5) & (report["Ρίσκο"] < 8)
maskiii = report["Ρίσκο"] >= 8

#βήμα δεύτερο - loc για να τοποθετηθεί στο ανάλογο κελί
report.loc[maski, "Αξιολόγηση Ρίσκου"] = "Χαμηλό"
report.loc[maskii, "Αξιολόγηση Ρίσκου"] = "Μεσαίο"
report.loc[maskiii, "Αξιολόγηση Ρίσκου"] = "Υψηλό"

print(report)

report.to_csv("customer_profitability_report.csv")

riskiest_client = report["Ρίσκο"].idxmax()
riskiest_client_value = report["Ρίσκο"].max()
print("Ο πιο ριψοκίνδυνος πελάτης είναι ο", riskiest_client, "με δείκτη ρίσκου:", riskiest_client_value)


