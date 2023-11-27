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
    pass
