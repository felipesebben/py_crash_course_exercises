import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

# Pass the CSV File Headers.
filename = 'data/ny_weather_1990-2022.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high and low temperatures from this file.
    dates, snowfall_vols = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            snowfall_vol = float(row[4]) # Convert to float, as data was stored as string.
        except ValueError:
            print(f"Missing data for {snowfall_vols}.")
        else:
            dates.append(current_date)
            snowfall_vols.append(snowfall_vol)

# Plot the high and low temperatures.
plt.style.use('seaborn-notebook')
fig, ax = plt.subplots()
ax.plot(dates, snowfall_vols, c='blue', alpha=0.5)

# Format plot.
title = "Daily Snowfall Volume, 1990 - 2022 \nNew York, NY"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.yaxis.set_ticks(np.arange(min(snowfall_vols), max(snowfall_vols)+1, 8))

plt.ylabel("Snowfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

