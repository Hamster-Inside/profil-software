import pandas as pd
from pandas_converters import parse_children

# Read CSV file
df = pd.read_csv('data/a/b/users_1.csv', delimiter=';', converters={'children': parse_children})

print(df)
