import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)
import pandas as pd

df = pd.read_csv("FuelConsumptionCo2.csv")
cdf = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]

cdf.hist()
plt.show()
