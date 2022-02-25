import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Pass the CSV File Headers.
filename = 'data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures from this file - extract row[5].
    dates, highs= [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5]) # Convert to integer, as data was stored as string.
        dates.append(current_date)
        highs.append(high)

# print(highs)

# Plot the high temperatures.
plt.style.use('seaborn-notebook')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

