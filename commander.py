from pandas_magic import PandasData
from db_context_manager import SQLiteDBManager
import os


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
        children = user_row['children'].values[0]
        if not self.data.has_children(user_row):
            print("You don't have children")
            return
        sorted_children = sorted(children, key=lambda x: x.get('name').lower())
        for child in sorted_children:
            print(f'{child.get('name')}, {child.get('age')}')


class FindSimilarChildrenCommand(Command):
    def execute(self, user_row=None):
        if not self.data.has_children(user_row):
            print("You don't have children")
            return
        user_children_ages = \
            [child['age'] for children_list in user_row['children'] for child in children_list]
        list_of_compatible_rows = [user_row.iloc[0]]
        for _, row in self.data.pandas_dataframe.iterrows():
            if not row.equals(user_row):
                if self.data.has_children(row):
                    current_user_children_ages = [child.get('age') for child in row['children']]
                    if any(element in current_user_children_ages for element in user_children_ages):
                        list_of_compatible_rows.append(row)
        if len(list_of_compatible_rows) > 1:
            for dataframe_row in list_of_compatible_rows:
                children = sorted(dataframe_row['children'],
                                  key=lambda x: x.get('name', '').lower())
                formatted_children = "; ".join([f"{child['name']}, "
                                                f"{child['age']}" for child in children])
                print(
                    f'{dataframe_row['firstname']}, {dataframe_row['telephone_number']}: '
                    f'{formatted_children}')
        else:
            print('There are no compatible children in the group')


class CreateDatabaseCommand(Command):
    def execute(self, user_row=None):
        db_name = 'user_data.db'
        if os.path.isfile(db_name):
            print(
                f'Database {db_name} already exists. If you want to refresh it, '
                f'you must delete current one and try again')
            return
        with SQLiteDBManager(db_name) as cursor:
            cursor.execute('''
                   CREATE TABLE IF NOT EXISTS child (
                       child_id INTEGER PRIMARY KEY,
                       name TEXT,
                       age INTEGER
                   )
               ''')



            print("SQLite DB created. But at the moment data is still used from files. DB is as a backup")
