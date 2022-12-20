import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import pandas as pd

# Instantiate rf
rf = RandomForestClassifier()
hyperparams = {
    'max_depth': 9,
    'n_estimators': 15,
    'min_samples_split': 3,
    'random_state': 0
}
             
class model():

    def __init__(self,X_train,y_train,modelsel,hyperparams = {}) -> None:
        self._hyperparams=hyperparams
        # if self._hyperparams is None:
        #     self._hyperparams = {}
        self.X_train=X_train
        self.y_train=y_train
        self.model=modelsel
        self.model.set_params(**self._hyperparams)
        self.train()

    def train(self):
        self.model = self.model.fit(self.X_train, self.y_train) 
        return None 

    def predict(self,X_test):
        self.y_test=self.model.predict(X_test)
        #self.test_proba=self.model.predict_proba(X_test)[:,1]
        return self.y_test



