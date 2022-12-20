import pandas as pd
import numpy as np

class time:
    
     def __init__(self, df, col):
        self.df = df
        self.df[col]=pd.to_datetime(df[col])
        self.col = col
    
     def year(self):
        self.df['timestamp_year'] = self.df[self.col].dt.year
        return self.df  
    
     def month(self):
        self.df['timestamp_month'] = self.df[self.col].dt.month
        return self.df  
    
     def day(self):
        self.df['timestamp_day'] = self.df[self.col].dt.day
        return self.df


class cluster:
    def __init__(self, df, target, group):
            self.df = df
            self.target = target
            self.group = group
        
    def make_cluster(self):

            df_level = self.df.groupby(self.group)[self.target].median().reset_index()
            df_level.columns = [self.group, self.group+'_encoded']
            self.df = self.df.merge(df_level)
            return self.df


class dummies:
    def __init__(self,df, cols): 
        self.df=df
        self.cols=cols
         
    def get_dum(self):
        self.df = self.df.join(pd.get_dummies(self.df[self.cols], drop_first=True))
        return self.df