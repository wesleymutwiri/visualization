import sys 
import csv 
import matplotlib.pyplot as plt

x= []
y= []

with open('wesley_data.csv', 'r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	csvfile.readline()
	for row in plots:
		x.append(row[0])
		y.append(float(row[1]))
plt.plot(x,y, label='Loaded from CSV file')
plt.xlabel('Dates')
plt.ylabel('Y')
plt.title("Sample trial in plotting graph")
plt.legend()
plt.show()
