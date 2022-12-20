    def get_roc_auc_score(self):
        '''
        Obtains the roc_auc metric for  test sets.
            
        '''
        # obtain scores
        test_auc = roc_auc_score(self.y_test, self.test_proba)
        
        return test_auc    