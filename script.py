""" Base file for console application start """
from argparse import ArgumentParser
from console_app import ConsoleApp
from pandas_magic import PandasData
from file_operations import get_file_list_deep


def main(app, args_from_user):
    """ main application, gathering all files from
    data and parsing it to pandas dataframe to work with methods"""
    files_with_data = get_file_list_deep('data', ['.csv', '.xml', '.json'])

    data = PandasData()

    for file in files_with_data:
        current_dataframe = data.convert_to_dataframe(file)
        data.add_dataframe(current_dataframe)

    data.clean_all_telephone_numbers()
    data.change_invalid_emails_to_none()
    data.delete_none_values(['telephone_number', 'email'])
    data.delete_duplicates_keep_first_based_on_created_at(['telephone_number', 'email'])

    app.run_command(args_from_user.command, args_from_user.login, args_from_user.password)


if __name__ == '__main__':
    console_app = ConsoleApp()
    parser = ArgumentParser(description='Data collecting App',
                            usage="Type in command line: METHOD --login LOGIN --password PASSWORD")
    parser.add_argument("command", choices=console_app.commands.keys(),
                        help="Specify the command to execute")
    parser.add_argument("--login", required=True, help="User login")
    parser.add_argument("--password", required=True, help="User password")
    parser._positionals.title = "Available methods"
    args, unknown_args = parser.parse_known_args()
    if unknown_args:
        print(f'Error: Nieznane metody: {' '.join(unknown_args)} '
              f'(Wpisz \"python script.py --help\" w celu pomocy)')
    else:
        args = parser.parse_args()
        main(console_app, args)
