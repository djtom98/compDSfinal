import numpy as np
import pandas as pd
import unittest
from pandas.testing import assert_frame_equal


from learnlibs.create_features import *


class TestCleanData(unittest.TestCase):
    def test_make_cluster(self):
        data=pd.DataFrame({'col1':[1, 1, 1, 5, 6, 7],
                           'col2':['a', 'a',  'a', 'b', 'b', 'b']})
        # print(data)
        
        cols=['col1', 'col2']
        col1 = data['col1']
        col2 = data['col2']
        expected_output=pd.DataFrame({'col1': [1, 1, 1, 5, 6, 7],
                           'col2': ['a', 'a', 'a', 'b', 'b', 'b'],
                           'col2_encoded': [1, 1, 1, 6, 6, 6]})
        output=cluster(data, 'col1', 'col2').make_cluster()
        #output=a.make_cluster(cols)
        assert_frame_equal(output,expected_output,check_dtype=False)


    def test_year(self):
        data=pd.DataFrame({'col1':['2002-05-10', '2022-04-11','2019-11-07']})

        expected_output= pd.DataFrame({'col1':['2002-05-10', '2022-04-11','2019-11-07'],
                                       'timestamp_year': [2002, 2022, 2019]})
        expected_output['col1'] =  pd.to_datetime(expected_output['col1'])
        output= time(data,'col1').year()
        assert_frame_equal(output,expected_output,check_dtype=False)
        
    def test_month(self):
        data=pd.DataFrame({'col1':['2002-05-10', '2022-04-11','2019-11-07']})

        expected_output= pd.DataFrame({'col1':['2002-05-10', '2022-04-11','2019-11-07'],
                                       'timestamp_month': [5 , 4, 11]})
        expected_output['col1'] =  pd.to_datetime(expected_output['col1'])
        output= time(data,'col1').month()
        assert_frame_equal(output,expected_output,check_dtype=False)
    
    def test_day(self):
        data=pd.DataFrame({'col1':['2002-05-10', '2022-04-11','2019-11-07']})

        expected_output= pd.DataFrame({'col1':['2002-05-10', '2022-04-11','2019-11-07'],
                                       'timestamp_day': [10 , 11, 7]})
        expected_output['col1'] =  pd.to_datetime(expected_output['col1'])
        output= time(data,'col1').day()
        assert_frame_equal(output,expected_output,check_dtype=False)

    # def test_get_dum(self):
    #     data=pd.DataFrame({'col1':[1]})
    #     expected_output=pd.DataFrame({'col1':[1],'1':[1]})
    #     output=dummies(data,['col1']).get_dum()
    #     self.assertEqual(expected_output,output)

