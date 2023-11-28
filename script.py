import pandas as pd
import pandas_magic
from file_searcher import get_file_list_deep

csv_files = get_file_list_deep('data', '.csv')
xml_files = get_file_list_deep('data', '.xml')
json_files = get_file_list_deep('data', '.json')

csv_dataframe = pandas_magic.get_dataframe_from_multiple_csv_files(csv_files)
xml_dataframe = pandas_magic.get_dataframe_from_multiple_xml_files(xml_files)
json_dataframe = pandas_magic.get_dataframe_from_multiple_json_files(json_files)

all_dataframes = pd.concat([csv_dataframe, xml_dataframe, json_dataframe], ignore_index=True)
all_dataframes['created_at'] = pd.to_datetime(all_dataframes['created_at'])

# drop duplicates
all_dataframes.drop_duplicates(subset='telephone_number', keep='first', inplace=True)
all_dataframes.drop_duplicates(subset='email', keep='first', inplace=True)

print(all_dataframes)
