import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Pass the CSV File Headers.
filename = 'data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get precipitation levels from this file - extract row[2].
    dates, rain_vols= [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain_vol = float(row[3]) # Convert to float, as data was stored as string.
        dates.append(current_date)
        rain_vols.append(rain_vol)

# Plot the rainfall levels.
plt.style.use('seaborn-notebook')
fig, ax = plt.subplots()
ax.plot(dates, rain_vols, c='blue', alpha=0.8)

# Format plot.
plt.title("Daily Rainfall Volume - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

