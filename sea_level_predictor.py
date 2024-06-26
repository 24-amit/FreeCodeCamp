import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Step 1: Import the data
df = pd.read_csv('epa-sea-level.csv')

# Step 2: Convert columns to numeric
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['CSIRO Adjusted Sea Level'] = pd.to_numeric(df['CSIRO Adjusted Sea Level'], errors='coerce')

# Step 3: Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Step 4: Calculate and plot the regression line for the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Extend the line to 2050
years_extended = np.arange(1880, 2051)
plt.plot(years_extended, intercept + slope * years_extended, color='red', label='Linear Fit (1880-2014)')

# Step 5: Restrict data to 2000 onwards and plot regression line if data exists
df_recent = df[df['Year'] >= 2000]
if not df_recent.empty:
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, intercept_recent + slope_recent * years_extended, color='green', label='Linear Fit (2000-Present)')

# Step 6: Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Step 7: Save and show the plot
plt.savefig('sea_level_prediction.png')
plt.show()
