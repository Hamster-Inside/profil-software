from pandas_magic import PandasData


class Command:
    def __init__(self):
        self.data = PandasData()

    def execute(self):
        pass


class PrintAllAccountsCommand(Command):
    def execute(self):
        print(self.data.pandas_dataframe)


class PrintOldestAccountCommand(Command):
    def execute(self):
        print("Printing the oldest account")


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
