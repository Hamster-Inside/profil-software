from pandas_magic import PandasData
from file_operations import get_file_list_deep

files_with_data = get_file_list_deep('data', ['.csv', '.xml', '.json'])

data = PandasData()

for file in files_with_data:
    current_dataframe = data.convert_to_dataframe(file)
    data.add_dataframe(current_dataframe)

data.clean_all_telephone_numbers()
data.change_invalid_emails_to_none()
data.delete_none_values(['telephone_number', 'email'])

data.delete_duplicates_keep_first_based_on_created_at(['telephone_number', 'email'])

print(data.pandas_dataframe)
