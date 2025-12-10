import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Load a NetCDF climate dataset
ds = xr.open_mfdataset("era5_data.nc")
print(ds)

# Load time series climate data
df = pd.read_csv("temperature_data.csv")

# Plot a temperature time series
plt.plot(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Over Time")
plt.show()
