from commander import PrintAllAccountsCommand, PrintOldestAccountCommand, GroupByAgeCommand, PrintChildrenCommand, \
    FindSimilarChildrenCommand, CreateDatabaseCommand
from pandas_magic import PandasData
import re


class ConsoleApp:
    def __init__(self):
        self.data = PandasData()
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
        if command:
            command.execute()
        else:
            print(f'Nie ma takiej metody: {command_name}')

    def authenticate(self, login, password):
        # Check if the login exists in the dataframe
        if self.is_phone_number(login):
            login_type = 'telephone_number'
        else:
            login_type = 'email'

        if login not in self.data.pandas_dataframe[login_type].values:
            return False

        # Check if the login and password match
        user_row = self.data.pandas_dataframe[self.data.pandas_dataframe[login_type] == login]
        return user_row['password'].values[0] == password

    @staticmethod
    def is_phone_number(input_string):
        pattern = r'^\d{9}$'
        match = re.match(pattern, input_string)
        return match is not None
