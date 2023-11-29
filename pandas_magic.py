""" Module for validation and creation of data to process to dataframe """

import re
import xml.etree.ElementTree as Et
import pandas as pd
from custom_exceptions import InvalidFileException
from validators.email_validator import EmailValidator
from validators.validator import ValidationError


class PandasData:
    """ class for operating on data files and converting them to pandas dataframe """
    supported_files = ['.csv', '.xml', '.json']
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PandasData, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.pandas_dataframe = pd.DataFrame()

    def convert_csv_to_dataframe(self, csv_file):
        csv_dataframe = pd.read_csv(csv_file, delimiter=';',
                                    converters={'children': self._parse_children_})
        return csv_dataframe

    @staticmethod
    def convert_xml_to_dataframe(xml_file):
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
    def convert_json_to_dataframe(json_file):
        json_dataframe = pd.read_json(json_file)
        return json_dataframe

    def convert_to_dataframe(self, file_to_convert):
        if file_to_convert.endswith('.csv'):
            result_dataframe = self.convert_csv_to_dataframe(file_to_convert)
        elif file_to_convert.endswith('.xml'):
            result_dataframe = self.convert_xml_to_dataframe(file_to_convert)
        elif file_to_convert.endswith('.json'):
            result_dataframe = self.convert_json_to_dataframe(file_to_convert)
        else:
            raise InvalidFileException(
                f'Allowed only files: '
                f'{self.supported_files}')
        return result_dataframe

    def add_dataframe(self, dataframe):
        self.pandas_dataframe = pd.concat([self.pandas_dataframe, dataframe], ignore_index=True)

    def get_dataframe(self):
        return self.pandas_dataframe

    def delete_duplicates_keep_first_based_on_created_at(self, list_of_col_names):
        self.pandas_dataframe['created_at'] = pd.to_datetime(self.pandas_dataframe['created_at'])
        for col_name in list_of_col_names:
            self.pandas_dataframe.drop_duplicates(subset=col_name, keep='first', inplace=True)
        self.pandas_dataframe = self.pandas_dataframe.reset_index(drop=True)

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

    def clean_all_telephone_numbers(self):
        self.pandas_dataframe['telephone_number'] = self.pandas_dataframe['telephone_number'].apply(
            self.clean_telephone_number)

    def delete_none_values(self, column_names):
        self.pandas_dataframe = self.pandas_dataframe.dropna(
            subset=column_names).reset_index(drop=True)

    def change_invalid_emails_to_none(self):
        self.pandas_dataframe['email'] = self.pandas_dataframe['email'].apply(
            self.validate_email)

    @staticmethod
    def validate_email(email):
        try:
            EmailValidator(email)
            return email
        except ValidationError:
            return None

    @staticmethod
    def clean_telephone_number(telephone_number):
        # Remove non-digit characters
        cleaned_number = re.sub(r'\D', '', str(telephone_number))

        # Remove leading zeros
        cleaned_number = cleaned_number.lstrip('0')

        # Ensure the number has 9 digits
        if len(cleaned_number) == 9:
            return cleaned_number
        if len(cleaned_number) > 9:
            return cleaned_number[-9:]
        return None

    @staticmethod
    def has_children(single_dataframe_or_series):
        if isinstance(single_dataframe_or_series, pd.DataFrame):
            children = single_dataframe_or_series['children'].values[0]
            if children:
                return True
        elif isinstance(single_dataframe_or_series, pd.Series):
            if len(single_dataframe_or_series['children']) > 0:
                return True
        return False
