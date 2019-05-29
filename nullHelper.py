class NullHelper:
    '''A class to help out your nulls!'''
    import pandas as pd 

    def __init__(self, df):
        self.df = df

    def check_for_values(self, value):
        '''let's you input common values that could be nans
        and will tell you how many a column has'''
        columns = self.columns
        if value in self.index:
            for column in columns:
                print(column, 'nulls:', self[self[column] == value].sum(),
                      'percentage of whole:', 
                      self[self[column] == value].sum()/self[column].count()*100, 
                      '%', '\n')
        else:
            print('No such value found')

    def replace_nulls(self, columns, before, after):
        for column in columns:
            self.column = self.column.replace(before, after)
        return self
