
import matplotlib.pyplot as plt
from pandas import read_csv
from numpy import arange
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.stats.diagnostic import acorr_ljungbox

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
plt.show()

# ~~~~3)
print("\n3)")

print("A stationary time series is a series whitch dosnt depend on the time. ")

# ~~~~4)
print("\n4)")

plt.plot(acf(logGNP, 40))
plt.show()
print("sdwfxgdswfqsrdf")

# ~~~~5)
print("\n5)")

plt.plot(acorr_ljungbox(logGNP, 40))
plt.show()

print("comment")
# ~~~~6)
print("\n6)")
print("commentl")

# B)
print("\nB)")
# ~~~~1)
print("1)")
diffGNP = [None]
prev = None
for e in logGNP:
    if prev is not None:
        diffGNP.append(e - prev)
    prev = e

series["diffGNP"] = diffGNP
print("diffGNP is the quarterly log return of GNP")

# ~~~~2)
plt.plot(years[1:], series["diffGNP"][1:])
plt.show()

# ~~~~3)
print("\n3)")
print("this series does indeed seem centered.")

# ~~~~4)
print("\n4)")
plt.plot(acf(series["diffGNP"][1:], 40))
plt.show()
plt.plot(pacf(series["diffGNP"][1:], 40))
plt.show()
print("???")