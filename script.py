import pandas as pd
from pandas_converters import parse_children
from file_searcher import get_file_list_deep

csv_files = get_file_list_deep('data', '.csv')
xml_files = get_file_list_deep('data', '.xml')
json_files = get_file_list_deep('data', '.json')


# df = pd.read_csv('data/a/b/users_1.csv', delimiter=';', converters={'children': parse_children})

# print(df)
