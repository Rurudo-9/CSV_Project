import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv","r")

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

# as an example
# mydate = '2018-07-01'
# converted_date = datetime.strptime(mydate, '%Y-%m-%d')

# print(converted_date)

# we call the method strptime() function ..

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)

# print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c = "red") # plot: line graph


fig.autofmt_xdate()


plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature(F)", fontsize = 12)
plt.tick_params(axis="both",  labelsize = 12)

#replace the number in specific date




plt.show()
