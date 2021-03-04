# try & except 

import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv","r")

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
lows = []
dates = []


# as an example
# mydate = '2018-01-01'
# converted_date = datetime.strptime(mydate, '%Y-%m-%d')

# print(converted_date)

# we call the method strptime() function ..

for row in csv_file:
    try: 
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2],'%Y-%m-%d')
        
    
    except ValueError:
        print(f"missing data for {converted_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

# print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c = "red") # plot: line graph
plt.plot(dates, lows, c='blue')


fig.autofmt_xdate()


# give pre-lsit
# alpha = 0.1 means the color is very light in the area
# alpha = 1 is the regular color

# we pass fill_between() the list dates for the x-values and then the high
# and lows
plt.fill_between(dates,highs,lows,facecolor= "blue", alpha=0.1)


plt.title("Daily high and low temperatures - 2018", fontsize = 16)
plt.xlabel("",fontsize = 12) 
plt.ylabel("Temperature(F)", fontsize = 12)
plt.tick_params(axis="both",  labelsize = 12)



#replace the number in specific date

# Matplotlib's pyplot API has a convenience function called subplots() which acts as a 
# utility wrapper and helps in creating common layouts of subplots, including the 
# enclosing figure object, in a single call.
'''
fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c='red')
a[1].plot(dates, lows, c='blue')

'''

plt.show()
