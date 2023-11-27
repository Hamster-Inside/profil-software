import pandas as pd
from pandas_converters import parse_children, get_dataframe_from_multiple_json_files, \
    get_dataframe_from_multiple_csv_files
from file_searcher import get_file_list_deep
import pandas as pd

csv_files = get_file_list_deep('data', '.csv')
xml_files = get_file_list_deep('data', '.xml')
json_files = get_file_list_deep('data', '.json')

csv_dataframe = get_dataframe_from_multiple_csv_files(csv_files)
# xml_dataframes =
json_dataframe = get_dataframe_from_multiple_json_files(json_files)

# Concatenate all dataframes
# all_dataframes = csv_dataframes + xml_dataframes + [json_dataframe]

# Merge dataframes, drop duplicates, and handle telephone numbers
# merged_df = pd.concat(all_dataframes, ignore_index=True)

print(csv_dataframe)

# df = pd.read_csv('data/a/b/users_1.csv', delimiter=';', converters={'children': parse_children})

# print(df)
