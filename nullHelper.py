class NullHelper:
    '''A class to help out your nulls!'''
    import pandas as pd 

    def __init__(self, df):
        self.df = df
        self.columns = df.columns
        self.values = df.values

    def check_for_values(self, value):
        '''let's you input common values that could be nans
        and will tell you how many a column has'''
        columns = self.columns
        if value in self.values:
            for column in columns:
                print(column,':', self[column][self[column] == value].count(),
                      'percentage of whole:', 
                      self[column][self[column] == value].count()/self[column].count()*100, 
                      '%')
        else:
            print('No such value found')

    def replace_nulls(self, column, before, after):
        '''Choose what columns, 
        what you want to change, 
        and what to change it to'''
        self[column] = self[column].replace(before, after)
        return self
