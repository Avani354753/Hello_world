import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller

# Load the data
file_path = 'D:\GEO 215\Week 10\Sentinel2_NDVI_TimeSeries_NorthBay.csv'
data = pd.read_csv(file_path)

# Convert the 'date' column to datetime format and sort by date
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by='date')

# Aggregate the data by date to get the average NDVI per day (since there might be multiple entries per date)
daily_data = data.groupby('date').agg({'NDVI': 'mean'}).reset_index()

# Set the date as the index
daily_data.set_index('date', inplace=True)

# Check for missing values in the NDVI data and fill them
daily_data['NDVI'].fillna(method='ffill', inplace=True)

# Perform seasonal decomposition with a weekly period (52 weeks)
decomposition = seasonal_decompose(daily_data['NDVI'], model='additive', period=52)

# Plot the decomposition
plt.figure(figsize=(12, 8))
decomposition.plot()
plt.show()

# Plot the ACF for the NDVI data
plt.figure(figsize=(12, 6))
plot_acf(daily_data['NDVI'], lags=50)
plt.show()

# Perform the ADF test on the NDVI time series
adf_result = adfuller(daily_data['NDVI'])

# Print the results
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Number of lags used:', adf_result[2])
print('Number of observations used:', adf_result[3])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'   {key}: {value}')

# Interpret the ADF test results
if adf_result[1] < 0.05:
    print("✅ The time series is stationary (p-value < 0.05).")
else:
    print("⚠️ The time series is non-stationary (p-value >= 0.05).")

# Save the ADF test results to a CSV file
adf_results_dict = {
    'Metric': ['ADF Statistic', 'p-value', 'Number of lags used', 'Number of observations used'] + list(adf_result[4].keys()),
    'Value': [adf_result[0], adf_result[1], adf_result[2], adf_result[3]] + list(adf_result[4].values())
}

adf_results_df = pd.DataFrame(adf_results_dict)
output_csv_path = r'D:\GEO 215\Week 10\ADF_Test_Results.csv'
adf_results_df.to_csv(output_csv_path, index=False)

print(f"✅ ADF test results saved to {output_csv_path}")

# Optional plot to visualize stationarity
plt.figure(figsize=(12, 6))
plt.plot(daily_data['NDVI'], label='NDVI')
plt.plot(daily_data['NDVI'].rolling(window=52).mean(), color='red', label='Rolling Mean (52 weeks)')
plt.title('NDVI Time Series with Rolling Mean')
plt.legend()
plt.show()
