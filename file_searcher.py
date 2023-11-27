from os import walk, path


def get_file_list_deep(from_dir, file_ending):
    """
    Gets all files from the given directory including, accessing every folder below
    :param from_dir: directory from where to start as str
    :param file_ending: file ending which we are looking for like '.csv'
    :return: list of files with given ending
    """
    w = walk(from_dir)
    temp_list = []
    for (dir_path, dirs, files) in w:
        for file in files:
            if file.endswith(file_ending):
                temp_list.append(path.join(dir_path, file).replace(path.sep, '/'))

    return temp_list
