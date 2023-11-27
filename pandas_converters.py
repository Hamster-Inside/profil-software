import pandas as pd


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
