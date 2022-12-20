from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score 

class calc_score:
    
     def __init__(self, y_test,y_pred):
        self.y_test=y_test
        self.y_pred=y_pred
    
     def r2(self):
        r2 = r2_score(self.y_test, self.y_pred)
        return r2  
    
     def mse(self):
        mse = mean_squared_error(self.y_test, self.y_pred) ** 0.5
        return mse
