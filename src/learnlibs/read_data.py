import pandas as pd
from sklearn.model_selection import train_test_split



class loader:
    
    def __init__(self, file):
        self.file = file
        self.load()
        
    def load(self):
        
        '''
        Read database.
        
        Parameters: 
            file: path to data
            
        Returns:
            df: database in pandas format
        '''
        
        self.df = pd.read_csv(self.file)
        return self.df
 
