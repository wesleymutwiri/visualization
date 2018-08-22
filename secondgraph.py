import sys 
import csv 
import matplotlib.pyplot as plt

a= []
b= []

with open('wesley_data.csv', 'r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	csvfile.readline()
	for row in plots:
		a.append(row[2])
		b.append(float(row[3]))
plt.plot(a,b, label='Loaded from CSV file')
plt.xlabel('A')
plt.ylabel('B')
plt.title("Sample trial in plotting graph")
plt.legend()
plt.show()