from pandas_magic import PandasData


class Command:
    def __init__(self):
        self.data = PandasData()

    def execute(self, user_row=None):
        pass


class PrintAllAccountsCommand(Command):
    def execute(self, user_row=None):
        print(len(self.data.pandas_dataframe))


class PrintOldestAccountCommand(Command):
    def execute(self, user_row=None):
        oldest_account_row = self.data.pandas_dataframe['created_at'].idxmin()
        print(f'name: {self.data.pandas_dataframe.loc[oldest_account_row, 'firstname']} \n'
              f'email_address: {self.data.pandas_dataframe.loc[oldest_account_row, 'email']} \n'
              f'created_at: {self.data.pandas_dataframe.loc[oldest_account_row, 'created_at']}')


class GroupByAgeCommand(Command):
    def execute(self, user_row=None):
        df_expanded = self.data.pandas_dataframe.explode('children')
        df_expanded = df_expanded[df_expanded['children'].notna()]
        df_expanded['age'] = df_expanded['children'].apply(lambda x: x['age'])
        child_counts = df_expanded['age'].value_counts().sort_values(ascending=True)
        for age, count in child_counts.items():
            print(f"age: {age}, count: {count}")


class PrintChildrenCommand(Command):
    def execute(self, user_row=None):
        print(user_row)


class FindSimilarChildrenCommand(Command):
    def execute(self, user_row=None):
        print("Finding similar children by age")


class CreateDatabaseCommand(Command):
    def execute(self, user_row=None):
        print("Creating a database")
