
import matplotlib.pyplot as plt
from pandas import read_csv
from numpy import arange
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from scipy.stats import shapiro


# A)
print("\nA)")
# ~~~~1)

series = read_csv('USeconomic.csv', header=0, index_col=[0 ,1])

# ~~~~2)

# print(type(series))
# print(series.head())
logGNP = series["log(GNP)"]
# print(logGNP.head())
years = arange(1954, 1988, 0.25)
# sample = logGNP[(1954, "Q1"): (1987, "Q3")]
plt.plot(years, logGNP)
plt.title("A-2")
plt.show()

# ~~~~3)
print("\n3)")

print("A stationary time series is a series whitch dosnt depend on the time. ")

# ~~~~4)
print("\n4)")

plt.title("A-4")

plt.plot(acf(logGNP, 135))
plt.show()

# ~~~~5)
print("\n5)")
plt.title("A-5")

plt.plot(acorr_ljungbox(logGNP,135)) # ????????????????????????????????? je sais pas
plt.show()

# ~~~~6)
print("\n6)")

# B)
print("\nB)")
# ~~~~1)
print("1)")
diffGNP = []
prev = 0
for e in logGNP:
    if(len(diffGNP)>0):
        diffGNP.append(e - prev)
    else:
        diffGNP.append(0)
    prev = e

print(diffGNP)
series["diffGNP"] = diffGNP
print("diffGNP is the quarterly log return of GNP")

# ~~~~2)
plt.title("B-2")

plt.plot(years[1:], series["diffGNP"][1:])
plt.show()

# ~~~~3)
print("\n3)")

# ~~~~4)
print("\n4)")
plt.title("B-4_acf")

plt.plot(acf(series["diffGNP"][1:], 40))
plt.show()
plt.title("B-4_pacf")

plt.plot(pacf(series["diffGNP"][1:], 40))
plt.show()

# ~~~~5)
print("\n5)")
abc= ARIMA(series["diffGNP"][1:],order =(0,0,2)).fit().predict(1)
print(abc)
plt.plot(years[1:len(series["diffGNP"])-1],abc)
plt.title("B-5")

plt.show()
# ~~~~6)
print("\n6)")


a=acorr_ljungbox(ARIMA(series["diffGNP"][1:],order =(0,0,1)).fit().predict(1))
aa=acorr_ljungbox(ARIMA(series["diffGNP"][1:],order =(0,0,2)).fit().predict(1))
aaa=acorr_ljungbox(ARIMA(series["diffGNP"][1:],order =(8,0,2)).fit().predict(1))
print("Box pierce, ARMA(0,1)",a)
print("Box pierce, ARMA(0,2)",aa)
print("Box pierce, ARMA(8,2)",aaa)



ba=shapiro(ARIMA(series["diffGNP"][1:],order =(0,0,1)).fit().predict(1))
baa=shapiro(ARIMA(series["diffGNP"][1:],order =(0,0,2)).fit().predict(1))
baaa=shapiro(ARIMA(series["diffGNP"][1:],order =(8,0,2)).fit().predict(1))
print("ARMA(0,1)",ba)
print("ARMA(0,2)",baa)
print("ARMA(8,2)",baaa)
# C)
print("\nC)")
# ~~~~1)
print("1)")
res01 = ARIMA(series["diffGNP"][1 :len(series["diffGNP"])-10], order=(0, 0, 1)).fit().predict(10)
res02 = ARIMA(series["diffGNP"][1 : len(series["diffGNP"])-10], order=(0, 0, 2)).fit().predict(10)
res82 = ARIMA(series["diffGNP"][1 : len(series["diffGNP"])-10], order=(8, 0, 2)).fit().predict(10)
plt.plot(years[1:len(series["diffGNP"])-20],res01)
plt.plot(years[1:len(series["diffGNP"])-20],res02)
plt.plot(years[1:len(series["diffGNP"])-20],res82)
plt.title("C-1_all")


plt.show()
plt.title("C-1_arma(0,1)")

plt.plot(years[1:len(series["diffGNP"])-20],res01)
plt.show()
plt.title("C-1_arma(0,2)")

plt.plot(years[1:len(series["diffGNP"])-20],res02)
plt.show()
plt.title("C-1_arma(8,2)")

plt.plot(years[1:len(series["diffGNP"])-20],res82)
plt.show()
# ~~~~2)
print("2)")

# D)
print("\nD)")
"""""
for i in range(5):&
    for y in range(5):
        res = ARIMA(series["diffGNP"][1: len(series["diffGNP"]) - 10], order=(i, 0, y)).fit().predict(10)
        plt.plot(years[1:len(series["diffGNP"]) - 20], res)

plt.show()
"""""
print("the end")