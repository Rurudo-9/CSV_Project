import csv

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",") # delimiter means the column separate by ","

header_row = next(csv_file ) # skip the first record on first row which is the header

#The enumerate() function returns both the index of each item and the value of each 
#item as you loop through a list.
# go to the first header line, the header row & tell the position of station/name/date... 
# show the index value of each loclation in the header

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

# print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt

plt.plot(highs, c = "red")
plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel("",fontsize = 16)
plt.ylabel("Temperature(F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize = 16)


plt.show()
