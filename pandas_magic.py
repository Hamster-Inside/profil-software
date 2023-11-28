import pandas as pd
import xml.etree.ElementTree as Et
from custom_exceptions import InvalidFileException


class PandasData:
    supported_files = ['.csv', '.xml', '.json']

    def __init__(self):
        self.pandas_dataframe = pd.DataFrame()

    def convert_csv_to_dataframe(self, csv_file):
        csv_dataframe = pd.read_csv(csv_file, delimiter=';', converters={'children': self._parse_children_})
        return csv_dataframe

    @staticmethod
    def convert_xml_to_dataframe(self, xml_file):
        tree = Et.parse(xml_file)
        root = tree.getroot()

        data = []
        for user_elem in root.findall('user'):
            user_data = {
                'firstname': user_elem.find('firstname').text,
                'telephone_number': user_elem.find('telephone_number').text,
                'email': user_elem.find('email').text,
                'password': user_elem.find('password').text,
                'role': user_elem.find('role').text,
                'created_at': user_elem.find('created_at').text
            }

            # Handle children
            children_elem = user_elem.find('children')
            if children_elem is not None:
                children_data = []
                for child_elem in children_elem.findall('child'):
                    child_data = {
                        'name': child_elem.find('name').text,
                        'age': int(child_elem.find('age').text)
                    }
                    children_data.append(child_data)
                user_data['children'] = children_data
            else:
                user_data['children'] = []

            data.append(user_data)

        return pd.DataFrame(data)

    @staticmethod
    def convert_json_to_dataframe(self, json_file):
        json_dataframe = pd.read_json(json_file)
        return json_dataframe

    def convert_to_dataframe(self, file):
        if file.endswith('.csv'):
            result_dataframe = self.convert_csv_to_dataframe(file)
        elif file.endswith('.xml'):
            result_dataframe = self.convert_xml_to_dataframe(file)
        elif file.endswith('.json'):
            result_dataframe = self.convert_json_to_dataframe(file)
        else:
            raise InvalidFileException(
                f'Allowed only files: {[file_extension for file_extension in self.supported_files]}')
        return result_dataframe

    def add_dataframe(self, dataframe):
        self.pandas_dataframe.append(dataframe, ignore_index=True, inplace=True)

    def get_dataframe(self):
        return self.pandas_dataframe

    def delete_duplicates(self, list_of_col_names):
        for col_name in list_of_col_names:
            self.pandas_dataframe.drop_duplicates(subset=col_name, keep='first', inplace=True)

   # def validate_col_data(self):


    @staticmethod
    def _parse_children_(children_str):
        if pd.isna(children_str) or children_str == '':
            return []

        children_list = []
        for child_info in children_str.split(','):
            parts = child_info.strip().split(' ')
            if len(parts) == 2:
                name, age = parts
                children_list.append({'name': name, 'age': int(age.strip('()'))})

        return children_list
