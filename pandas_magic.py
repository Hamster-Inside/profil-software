import pandas as pd
import xml.etree.ElementTree as ET


def parse_children(children_str):
    if pd.isna(children_str) or children_str == '':
        return []

    children_list = []
    for child_info in children_str.split(','):
        parts = child_info.strip().split(' ')
        if len(parts) == 2:
            name, age = parts
            children_list.append({'name': name, 'age': int(age.strip('()'))})

    return children_list


def xml_to_dataframe(file_path):
    tree = ET.parse(file_path)
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


def get_dataframe_from_multiple_json_files(json_files):
    all_json_dataframes = []
    for json_file in json_files:
        json_dataframe = pd.read_json(json_file)
        all_json_dataframes.append(json_dataframe)
    final_dataframe = pd.concat(all_json_dataframes, ignore_index=True)
    return final_dataframe


def get_dataframe_from_multiple_csv_files(csv_files):
    all_csv_dataframes = []
    for csv_file in csv_files:
        csv_dataframe = pd.read_csv(csv_file, delimiter=';', converters={'children': parse_children})
        all_csv_dataframes.append(csv_dataframe)
    final_dataframe = pd.concat(all_csv_dataframes, ignore_index=True)
    return final_dataframe


def get_dataframe_from_multiple_xml_files(xml_files):
    all_xml_dataframes = []
    for xml_file in xml_files:
        xml_dataframe = xml_to_dataframe(xml_file)
        all_xml_dataframes.append(xml_dataframe)
    final_dataframe = pd.concat(all_xml_dataframes, ignore_index=True)
    return final_dataframe
