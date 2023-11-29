from pandas_magic import PandasData


class Command:
    def __init__(self):
        self.data = PandasData()

    def execute(self):
        pass


class PrintAllAccountsCommand(Command):
    def execute(self):
        print(len(self.data.pandas_dataframe))


class PrintOldestAccountCommand(Command):
    def execute(self):
        oldest_account_row = self.data.pandas_dataframe['created_at'].idxmin()
        print(f'name: {self.data.pandas_dataframe.loc[oldest_account_row, 'firstname']} \n'
              f'email_address: {self.data.pandas_dataframe.loc[oldest_account_row, 'email']} \n'
              f'created_at: {self.data.pandas_dataframe.loc[oldest_account_row, 'created_at']}')


class GroupByAgeCommand(Command):
    def execute(self):
        print("Grouping by age")


class PrintChildrenCommand(Command):
    def execute(self):
        print("Printing children")


class FindSimilarChildrenCommand(Command):
    def execute(self):
        print("Finding similar children by age")


class CreateDatabaseCommand(Command):
    def execute(self):
        print("Creating a database")
