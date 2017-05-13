import numpy as np
import pandas as pd
from time import time
from IPython.display import display
import visuals as vs

data = pd.read_csv("census.csv")
display(data.head(n=1))

n_records = data.shape[0]

n_greater_50k = data.loc[lambda df: df.income == '>50K', :].shape[0]

n_at_most_50k = data.loc[lambda df: df.income == '<=50K', :].shape[0]

greater_percent = n_greater_50k * 100. / n_records

print "Total number of records: {}".format(n_records)
print "Individuals making more than $50,000: {}".format(n_greater_50k)
print "Individuals making at most $50,000: {}".format(n_at_most_50k)
print "Percentage of individuals making more than $50,000: {:.2f}%".format(greater_percent)



