#! /usr/bin/env python

"""This script introduces some data handling and plotting tools."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')

# Import the data from a csv file using pandas which returns the data
# as a dataframe object. Dataframes are easier to use in data handling.
# If we know the data already contains dates, pandas allows us to parse
# the dates and therefore the data is handled as a timeseries set.


def get_data(path):
    """
    Fetch the dataset.

    Path: A path to the dataset
    """
    return pd.read_csv(path, parse_dates=True, index_col=0)


data = get_data("./wesley_data.csv")

# If the data in the Dataframe is named we can obtain the names
dataname = data.columns.tolist()

# We can plot a simple plot to visualise the dataset
plt.plot(data)
plt.savefig('graphs/mp_graph.png')

# Using seaborn to plot the same dataset
sns.lineplot(data=data)
plt.savefig('graphs/sns_graph.png')

if __name__ == '__main__':
    print("======= Test section =======")
    data = get_data('./wesley_data.csv')
    print("Data \n{}\n".format(data.head()))  # Show data sample
    print("basic statistics of the dataset\n{}".format(data.describe()))
