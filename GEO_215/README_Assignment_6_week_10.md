# NDVI Time Series Analysis and Stationarity Testing

This script performs time series analysis on NDVI (Normalized Difference Vegetation Index) data, including seasonal decomposition, autocorrelation analysis, and stationarity testing using the Augmented Dickey-Fuller (ADF) test. The results of the ADF test are saved to a CSV file for further analysis.

## Features

1. **Data Preprocessing**:
   - Converts the `date` column to datetime format and sorts the data by date.
   - Aggregates NDVI values by date to calculate daily averages.
   - Handles missing values in the NDVI data using forward fill.

2. **Seasonal Decomposition**:
   - Decomposes the NDVI time series into trend, seasonal, and residual components using a weekly period (52 weeks).
   - Visualizes the decomposition results.

3. **Autocorrelation Analysis**:
   - Plots the autocorrelation function (ACF) for the NDVI data to analyze temporal dependencies.

4. **Stationarity Testing**:
   - Performs the Augmented Dickey-Fuller (ADF) test to check if the NDVI time series is stationary.
   - Interprets the ADF test results:
     - **p-value < 0.05**: The time series is stationary.
     - **p-value ≥ 0.05**: The time series is non-stationary.
   - Saves the ADF test results to a CSV file.

5. **Visualization**:
   - Plots the NDVI time series with a rolling mean to visualize stationarity.

## Requirements

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `matplotlib`
  - `statsmodels`

Install the required libraries using:
```bash
pip install pandas matplotlib statsmodels

Usage
Input Data:

The script expects a CSV file containing NDVI data with at least two columns:
date: The date of the observation.
NDVI: The NDVI value for the corresponding date.
Update the file_path variable with the path to your input CSV file

Run the Script:

Execute the script in your Python environment.
Output:

The script generates the following outputs:
Seasonal decomposition plots.
Autocorrelation function (ACF) plot.
ADF test results printed to the console.
A CSV file (ADF_Test_Results.csv) containing the ADF test results saved to the specified output path

Interpretation:

The ADF test results indicate whether the NDVI time series is stationary or non-stationary based on the p-value.
Example Output
ADF Test Results (Console):

ADF Statistic: -3.456
p-value: 0.012
Number of lags used: 5
Number of observations used: 100
Critical Values:
   1%: -3.500
   5%: -2.890
   10%: -2.580
✅ The time series is stationary (p-value < 0.05).

CSV File:
Metric	Value
ADF Statistic	-3.456
p-value	0.012
Number of lags used	5
Number of observations used	100
1%	-3.500
5%	-2.890
10%	-2.580
Notes
Ensure the input CSV file is properly formatted with valid date and NDVI columns.
Adjust the seasonal decomposition period (period=52) based on the frequency of your data (e.g., weekly, monthly).