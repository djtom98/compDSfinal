class model():

    def __init__(self, train, modelsel, x_cols, target) -> None:
        self._x_cols = x_cols
        self._target = target
#        self._hyperparams = hyperparams
#         if hyperparams is None:
#            hyperparams = {}
        self.model = modelsel
        self.train(train)

    def train(self, train):
        '''
        Train the model
        Parameters:
            train: train data as input
        '''
        X_train = train[self._x_cols]
        y_train = train[self._target]
        self.model_fit = self.model.fit(X_train, y_train) 
        return None 

    def predict(self, test):
        '''
        Predict results from test data
        
        Parameters:
            test: input data for prediction
        '''
        X_test = test[self._x_cols]
        return self.model_fit.predict_proba(X_test[self._x_cols])