from commander import PrintAllAccountsCommand, PrintOldestAccountCommand, GroupByAgeCommand, PrintChildrenCommand, \
    FindSimilarChildrenCommand, CreateDatabaseCommand


class ConsoleApp:
    def __init__(self):
        self.commands = {
            'print-all-accounts': PrintAllAccountsCommand(),
            'print-oldest-account': PrintOldestAccountCommand(),
            'group-by-age': GroupByAgeCommand(),
            'print-children': PrintChildrenCommand(),
            'find-similar-children': FindSimilarChildrenCommand(),
            'create-database': CreateDatabaseCommand(),
        }

    def run_command(self, command_name):
        command = self.commands.get(command_name)
        if command:
            command.execute()
        else:
            print(f'Nie ma takiej metody: {command_name}')

