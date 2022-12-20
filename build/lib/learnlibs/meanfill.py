import pandas as pd
import numpy as np


class nan_filler:
    
        def __init__(self, df, cols):
            self.df = df
            self.cols = cols
        
        def fill_means(self):
            
            '''
            Fill NaN with the mean value of the column in the given columns.
            
            Parameters: 
                df (dataframe): dataframe to fill NaNs for
                col (list): target columns to fill NaNs for
                
            Returns:
                df: dataframe with filled NaN in target columns
            '''
            
            self.df.loc[:,self.cols] = self.df.loc[:,self.cols].fillna(self.df.loc[:,self.cols].mean())
            return self.df
        
        
        def fill_unavailable(self):
            
            '''
            Fill NaN with the "Unavailable" for the non-numeric columns.
            
            Parameters: 
                df (dataframe): dataframe to fill NaNs for
                col (list): target columns to fill NaNs for
                
            Returns:
                df: dataframe with filled NaN in target columns
            '''
            
            self.df.loc[:,self.cols] = self.df.loc[:,self.cols].fillna("Unavailable")
            return self.df