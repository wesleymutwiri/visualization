#! /usr/bin/env python

"""This script introduces some data handling and plotting tools."""
import pandas as pd
import matplotlib.pyplot as plt

# Import the data from a csv file using pandas


def get_data(path):
	"""Fetch the data."""
	return pd.read_csv(path, parse_dates=True, index_col=0)


data = get_data('./wesley_data.csv')

fig, ax = plt.subplots()

for name in data.columns.tolist():
	ax.plot(data[name].index, data[name], label=name)

plt.xlabel('Date')
plt.ylabel('Y')
plt.title("Sample trial in plotting graph")
plt.legend()
plt.savefig('graphs/all_items.png')

if __name__ == '__main__':
	print("Data sample \n{}\n".format(data.head()))
	print("Basic statistics of the data\n{}\n".format(data.describe()))
