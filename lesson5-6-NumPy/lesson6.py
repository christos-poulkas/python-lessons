import numpy as np

dates = np.genfromtxt('dailyprices.csv',
                      delimiter=',',
                      skip_header=1,
                      usecols=0,
                      dtype=str)

data = np.genfromtxt('dailyprices.csv',
                       delimiter=',',
                       skip_header=1,
                       usecols=(1,2,3,4,5),
                       dtype=float)

print(dates.shape)   # πρέπει να δείξει (γραμμές, 5)

APPL = data[:, 0]
AMZN = data[:, 1]
KO = data[:, 2]
MSFT = data[:, 3]
NKE = data[:, 4]

DATE = dates[:]

print(APPL.max())
print(AMZN.max())
print(KO.max())
print(MSFT.max())
print(NKE.max())

APPL_max = APPL.max()
AMZN_max = AMZN.max()
KO_max = KO.max()
MSFT_max = MSFT.max()
NKE_max = NKE.max()

index = APPL.argmax()
date_appl = DATE[index]
print (date_appl)

index = AMZN.argmax()
date_amzn = DATE[index]
print (date_amzn)

index = KO.argmax()
date_ko = DATE[index]
print (date_ko)

index = MSFT.argmax()
date_msft = DATE[index]
print (date_msft)

index = NKE.argmax()
date_nke = DATE[index]
print (date_nke)

mean_avg_APPL = APPL.mean()
print(mean_avg_APPL)

std_APPL = APPL.std()
print(std_APPL)


#4.
above_mean_APPL = []
for i in APPL:
    if i > mean_avg_APPL:
        above_mean_APPL.append(float(i))

print(above_mean_APPL)

#5.
above_mean_std_APPL = []
for i in APPL:
    if i > mean_avg_APPL + std_APPL:
        above_mean_std_APPL.append(float(i))

print(above_mean_std_APPL)

#6.
above_mean_3std_APPL = []
for i in APPL:
    if i > mean_avg_APPL + (3 * std_APPL):
        above_mean_3std_APPL.append(float(i))

print(above_mean_3std_APPL)




