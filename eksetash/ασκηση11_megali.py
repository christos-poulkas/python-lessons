import pandas as pd

df = pd.read_csv("../lesson7-pandas/sales_transactions.csv", sep=",", encoding ="utf-8")
print(df)

df_valid = df[(df["Έσοδα"] > 0) & (df["Κόστος"] >= 0)].copy()
df_valid.reset_index(drop=True, inplace=True)

print(df_valid)

df_valid["Κέρδος"] = df_valid["Έσοδα"] - df_valid["Κόστος"]

df_valid["ΠεριθώριοΚέρδους"] = (
    df_valid["Κέρδος"].div(df_valid["Έσοδα"]).fillna(0) * 100
)

print(df_valid.head())

df_valid["Εκκρεμή_Έσοδα"] = df_valid["Έσοδα"].where(
    df_valid["ΚατάστασηΠληρωμής"] == "Εκκρεμεί", 0
)

report = ( #αναφορά πελάτη
    df_valid
    .groupby("Πελάτης", as_index=False)
    .agg(
        Συνολικά_Έσοδα=("Έσοδα", "sum"),
        Συνολικό_Κόστος=("Κόστος", "sum"),
        Συνολικό_Κέρδος=("Κέρδος", "sum"),
        Μέσο_Περιθώριο_Κέρδους=("ΠεριθώριοΚέρδους", "mean"),
        Εκκρεμή_Έσοδα=("Εκκρεμή_Έσοδα", "sum"),
    )
)

print(report)


def calculate_risk(row): #υπολογισμός βαθμού ρίσκου
    score = 0

    if row["Εκκρεμή_Έσοδα"] > 0.30 * row["Συνολικά_Έσοδα"]:
        score += 5

    if row["Μέσο_Περιθώριο_Κέρδους"] < 10:
        score += 3

    if row["Συνολικό_Κέρδος"] < 0:
        score += 5

    return score

def risk_category(score):
    if score < 5:
        return "Χαμηλό"
    elif 5 <= score <= 8:
        return "Μεσαίο"
    else:
        return "Υψηλό"

report["Βαθμοί_Ρίσκου"] = report.apply(calculate_risk, axis=1)
report["Αξιολόγηση_Ρίσκου"] = report["Βαθμοί_Ρίσκου"].apply(risk_category)

print(report)

report.to_csv("customer_profitability_report.csv", index=False)

max_risk_customer = report.loc[report["Βαθμοί_Ρίσκου"].idxmax()]

print("Πελάτης με το μεγαλύτερο Βαθμό Ρίσκου:")
print(max_risk_customer[["Πελάτης", "Βαθμοί_Ρίσκου", "Αξιολόγηση_Ρίσκου"]])