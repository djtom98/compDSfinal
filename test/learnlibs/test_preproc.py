#%%
import pandas as pd
import numpy as np
import unittest
from pandas.testing import assert_frame_equal


# def drop_nan(df: pd.DataFrame, cols: list):
#     '''
#     Remove those rows that contain NaN values in the given columns.
    
#     Parameters: 
#         df (dataframe): dataframe to remove rows for
#         cols (list): target columns to remove rows for
        
#     Returns:
#          cleaned_df: dataframe with removed rows in target columns
#     '''
#     cleaned_df = df.dropna(axis=0, subset=cols, how='any')
#     return cleaned_df
#%%
from learnlibs.preproc import *

#%%

class TestCleanData(unittest.TestCase):
    def test_drop_nan(self):
        data=pd.DataFrame({'col1':[1,2,3,4,5,np.nan]})
        # print(data)

        cols=['col1']
        a=remove_nan(data,cols)
        expected_output=pd.DataFrame({'col1':[1,2,3,4,5]})
        output=a.drop_nan()
        assert_frame_equal(output,expected_output,check_dtype=False)


