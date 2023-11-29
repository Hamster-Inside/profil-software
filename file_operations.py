""" Custom module for operations on files """
from os import walk, path


def get_file_list_deep(from_dir, file_endings):
    """
    Gets all files from the given directory including, accessing every folder below
    :param from_dir: directory from where to start as str
    :param file_endings: file ending which we are looking for
            like '.csv' or list like ['.csv', '.json']
    :return: list of files with given ending
    """
    w = walk(from_dir)
    temp_list = []

    if isinstance(file_endings, str):
        file_endings = [file_endings]

    for (dir_path, _, files) in w:
        for file in files:
            if any(file.endswith(ending) for ending in file_endings):
                temp_list.append(path.join(dir_path, file).replace(path.sep, '/'))

    return temp_list
