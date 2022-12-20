
import pandas as pd
import numpy as np

class remove_nan:
    
        def __init__(self, df, cols):
            self.df = df
            self.cols = cols
            
        def drop_nan(self):
            
            '''
            Remove those rows that contain NaN values in the given columns.
            
            Parameters: 
                df (dataframe): dataframe to remove rows for
                cols (list): target columns to remove rows for
                
            Returns:
                 cleaned_df: dataframe with removed rows in target columns
            '''
            
            self.cleaned_df = self.df.dropna(axis = 0, subset = self.cols, how = 'any')
            return self.cleaned_df
            
class fill_nan:
    
        def __init__(self, df, cols):
            self.df = df
            self.cols = cols
            self.fill_nan_mean(self.cols)
        
        def fill_nan_mean(self, cols):
            
            '''
            Fill NaN with the mean value of the column in the given columns.
            
            Parameters: 
                df (dataframe): dataframe to fill NaNs for
                cols (list): target columns to fill NaNs for
                
            Returns:
                df: dataframe with filled NaN in target columns
            '''
            
            self.df.loc[:,cols] = self.df.loc[:,cols].fillna(self.df.mean())
