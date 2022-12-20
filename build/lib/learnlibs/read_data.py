# Part A

import pandas as pd
from sklearn.model_selection import train_test_split



class loader():
    
    def __init__(self, file):
        self.file = file
        self.load()
        self.split()
        
    def load(self):
        
        '''
        Read database.
        
        Parameters: 
            file: path to data
            
        Returns:
            df: database in pandas format
        '''
        
        self.df = pd.read_csv(self.file, index_col=0)
        return self.df
      

    def split(self):

        
        '''
        Split data between train and test using sklearn.model_selection.train_test_split.
        
        Parameters: 
            df: dataframe to split data for analysis 
            
        Returns:
            train: splitted dataframe for training models
            test: splitted dataframe for training models
            
        '''
        
        seed = 2
        self.train, self.test = train_test_split(self.df, test_size=0.3, random_state=seed)

        return self.train, self.test