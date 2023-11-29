from commander import PrintAllAccountsCommand, PrintOldestAccountCommand, GroupByAgeCommand, PrintChildrenCommand, \
    FindSimilarChildrenCommand, CreateDatabaseCommand
from pandas_magic import PandasData
import re


class ConsoleApp:
    def __init__(self):
        self.data = PandasData()
        self.is_admin = False
        self.admin_only_command_list = ['print-all-accounts', 'print-oldest-account', 'group-by-age']
        self.commands = {
            'print-all-accounts': PrintAllAccountsCommand(),
            'print-oldest-account': PrintOldestAccountCommand(),
            'group-by-age': GroupByAgeCommand(),
            'print-children': PrintChildrenCommand(),
            'find-similar-children': FindSimilarChildrenCommand(),
            'create-database': CreateDatabaseCommand(),
        }

    def run_command(self, command_name, login, password):
        # Check authentication
        if not self.authenticate(login, password):
            print("Invalid Login")
            return
        command = self.commands.get(command_name)
        if command_name in self.admin_only_command_list and not self.is_admin:
            print('Must be admin to use this method')
            return
        if command:
            command.execute()
        else:
            print(f'Nie ma takiej metody: {command_name}')

    def authenticate(self, login, password):

        if self.is_phone_number(login):
            login_type = 'telephone_number'
        else:
            login_type = 'email'

        if login not in self.data.pandas_dataframe[login_type].values:
            return False

        user_row = self.data.pandas_dataframe[self.data.pandas_dataframe[login_type] == login]
        if user_row['role'].values[0] == 'admin':
            self.is_admin = True
        return user_row['password'].values[0] == password

    @staticmethod
    def is_phone_number(input_string):
        pattern = r'^\d{9}$'
        match = re.match(pattern, input_string)
        return match is not None
