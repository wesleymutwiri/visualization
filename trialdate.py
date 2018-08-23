import sys 
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np 
# creating empty lists for storing of data from the csv files
dates= []
fixs= []
kixs=[]
sp5s= []
 
# opening the csv file containing the data
with open('wesley_data.csv','r') as csvfile:
    
    #reading of the csv file
    plots = csv.reader(csvfile)
    
    # function used to skip the first line of the CSV file
    csvfile.readline()
    
    # looping through the different elements in the CSV file
    for Date, fix, kix,sp5 in plots:
            # appending all CSV data into the different lists created above
            dates.append(datetime.strptime(Date, '%Y-%m-%d'))
            fixs.append(fix)
            kixs.append(kix)
            sp5s.append(sp5)

# converting all the lists created into numpy array so as to plot graph 
datex=np.array(dates)
fixx=np.array(fixs)
kixx=np.array(fixs)
sp5x=np.array(sp5s)

# plotting different graphs with the same x axis
plt.plot_date(datex, fixx, label='dates fix1', color='orange', fmt='-')

# different color coding to differentiate the different graphs being calculated
plt.plot_date(datex, kixx, label='dates kix1', color='blue', fmt='-')

# using same y axis to get graph plot against date as the x axis
plt.plot_date(datex,sp5x, label='dates sp5', color='green', fmt='-')

# 
plt.legend(bbox_to_anchor=(0., 1.02,1.,.102), loc=3, ncol=4, borderaxespad=0)
plt.show()


