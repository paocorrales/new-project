import xarray as xr

# Load a NetCDF climate dataset
ds = xr.open_mfdataset("era5_data.nc")
print(ds)
