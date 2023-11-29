""" Console application base class for sending commander method to execute """

import re
from commander import (PrintAllAccountsCommand, PrintOldestAccountCommand,
                       GroupByAgeCommand, PrintChildrenCommand,
                       FindSimilarChildrenCommand, CreateDatabaseCommand)
from pandas_magic import PandasData


class ConsoleApp:
    """ Command sending class """
    def __init__(self):
        self.data = PandasData()
        self.is_admin = False
        self.user_row = None
        self.admin_only_command_list = \
            ['print-all-accounts', 'print-oldest-account', 'group-by-age']
        self.commands = {
            'print-all-accounts': PrintAllAccountsCommand(),
            'print-oldest-account': PrintOldestAccountCommand(),
            'group-by-age': GroupByAgeCommand(),
            'print-children': PrintChildrenCommand(),
            'find-similar-children-by-age': FindSimilarChildrenCommand(),
            'create_database': CreateDatabaseCommand(),
        }

    def run_command(self, command_name, login, password):
        """ execution of a method """
        # Check authentication
        if not self.authenticate(login, password):
            print("Invalid Login")
            return
        command = self.commands.get(command_name)
        if (command_name in self.admin_only_command_list
                and not self.user_row['role'].values[0] == 'admin'):
            print('Must be admin to use this method')
            return
        if command:
            command.execute(self.user_row)
        else:
            print(f'Nie ma takiej metody: {command_name}')

    def authenticate(self, login, password):
        """ user authentication for existing login and valid password """
        if self.is_phone_number(login):
            login_type = 'telephone_number'
        else:
            login_type = 'email'
        if login not in self.data.pandas_dataframe[login_type].values:
            return False
        self.user_row = self.data.pandas_dataframe[self.data.pandas_dataframe[login_type] == login]
        return self.user_row['password'].values[0] == password

    @staticmethod
    def is_phone_number(input_string):
        """ method checking if incoming string is a phone or email """
        pattern = r'^\d{9}$'
        match = re.match(pattern, input_string)
        return match is not None
