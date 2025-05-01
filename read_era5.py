import xarray as xr
import matplotlib.pyplot as plt
import numpy

# Load a NetCDF climate dataset
ds = xr.open_mfdataset("era5_data.nc")
print(ds)

# Plot a temperature time series
plt.plot(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Over Time")
plt.show()
