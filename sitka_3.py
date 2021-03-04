# 1) changing the file to include all the data for the year of 2018
# 2) change the title to -Daily and low high temperatures - 2018
# 3) extract low tempts from the file and add to chart
# 4) shade in the area between high and low


import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv","r") 

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file )

print(type(header_row))

#The enumerate() function returns both the index of each item and the value of each 
#item as you loop through a list.
# go to the first header line, the header row & tell the position of station/name/date... 
# show the index value of each loclation in the header

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []

# as an example
# mydate = '2018-07-01'
# converted_date = datetime.strptime(mydate, '%Y-%m-%d')

# print(converted_date)

# we call the method strptime() function ..

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)

# print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c = "red") # plot: line graph
plt.plot(dates, lows, c='blue')

fig.autofmt_xdate()

plt.fill_between(dates,highs,lows,facecolor= "blue", alpha=0.1)


plt.title("Daily high and low temperatures - 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature(F)", fontsize = 12)
plt.tick_params(axis="both",  labelsize = 12)

#replace the number in specific date




plt.show()


fig2, a = plt.subplots(2)
a[0].plot(dates,highs,c = 'red')
a[1].plot(dates,lows,c='blue')

plt.show()