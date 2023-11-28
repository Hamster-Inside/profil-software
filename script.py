import pandas as pd
import pandas_magic
from file_searcher import get_file_list_deep

csv_files = get_file_list_deep('data', '.csv')
xml_files = get_file_list_deep('data', '.xml')
json_files = get_file_list_deep('data', '.json')

csv_dataframe = pandas_magic.get_dataframe_from_multiple_csv_files(csv_files)
xml_dataframe = pandas_magic.get_dataframe_from_multiple_xml_files(xml_files)
json_dataframe = pandas_magic.get_dataframe_from_multiple_json_files(json_files)

# Concatenate all dataframes
#all_dataframes = csv_dataframe + xml_dataframe + json_dataframe

# Merge dataframes, drop duplicates, and handle telephone numbers
# merged_df = pd.concat(all_dataframes, ignore_index=True)

print(xml_dataframe)
