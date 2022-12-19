
import pandas as pd
import numpy as np


class nan_filler:
    
        def __init__(self, df):
            self.df = df
        
        def fill_means(self, col):
            
            '''
            Fill NaN with the mean value of the column in the given columns.
            
            Parameters: 
                df (dataframe): dataframe to fill NaNs for
                col (list): target columns to fill NaNs for
                
            Returns:
                df: dataframe with filled NaN in target columns
            '''
            
            self.df.loc[:,col] = self.df.loc[:,col].fillna(self.df.loc[:,col].mean())
            return self.df