import csv
from datetime import datetime

from matplotlib import pyplot as plt

def get_data(filename, dates, highs, lows, date_index, high_index,
        low_index):
    
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        
        for row in reader:
            converted_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {converted_date}")
            else:
                dates.append(converted_date)
                highs.append(high)
                lows.append(low)

# Get Sitka data.
filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_data(filename, dates, highs, lows, date_index=2, high_index=5,
        low_index=6)

#plot Sitka weather data .

fig, ax = plt.subplots(2)
ax[0].plot(dates, highs, c='red', alpha=0.6)
ax[0].plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get Death Valley DATA.
filename = 'death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_data(filename, dates, highs, lows, date_index=2, high_index=4,
        low_index=5)

# Add Death Valley plot.
ax[1].plot(dates, highs, c='red', alpha=0.6)
ax[1].plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Format plot.
title = "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()


