import numpy as np
import pandas as pd
import unittest
from pandas.testing import assert_frame_equal


from learnlibs import meanfill



class TestCleanData(unittest.TestCase):
    def test_fill_unavailable(self):
        data=pd.DataFrame({'col1':["Red", "Green", np.nan, "Blue"]})
        # print(data)
        
        cols=['col1']
        expected_output=pd.DataFrame({'col1':["Red", "Green", "Unavailable", "Blue"]})
        a=meanfill.nan_filler(data,cols)
        output=a.fill_unavailable()
        assert_frame_equal(output,expected_output,check_dtype=False)
