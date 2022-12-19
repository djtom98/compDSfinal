
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

class transformer(ABC):

    def __init__(self, df, col:list) -> None:
        self.df = df
        self.col = col

    @abstractmethod
    def apply_transform(self):
        return NotImplementedError

class log(transformer):

    def apply_transform(self):
        '''
        Apply logarithms to some of the columns in the dataset.
        
        Parameters:
            df: dataframe to be treated
            col: feature to be transformed
        Returns:
            Transformed dataframe
        '''
        self.df.loc[:,self.col] = self.df.loc[:,self.col].apply(lambda x: np.log10(x))
        return self.df
    
class levels(transformer):

    def apply_transform(self):
        '''
        Apply a transformation to return to original logged values.
        
        Parameters:
            df: dataframe to be treated
            col: feature to be transformed
        Returns:
            Transformed dataframe
        '''
        self.df.loc[:,self.col] = self.df.loc[:,self.col].apply(lambda x: np.exp(x))
        return self.df


class nan_dropper():
    
    def __init__(self, df):
        self.df = df
        
    def drop_nan(self, col):
        
        '''
        Remove those rows that contain NaN values in the given columns.
        
        Parameters: 
            df (dataframe): dataframe to remove rows for
            col (list): target columns to remove rows for
            
        Returns:
                cleaned_df: dataframe with removed rows in target columns
        '''
        
        self.cleaned_df = self.df.dropna(axis=0, subset=col, how='any')
        return self.cleaned_df
    
    
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

