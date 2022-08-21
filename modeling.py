def confusion(TN, TP, FN, FP):
    acc = (TP+TN)/(TP+TN+FP+FN)
    pre = (TP/(TP+FP))
    NPV = (TN/(TN+FN))
    rec = (TP/(TP+FN))
    spe = (TN/(TN+FP))
    f1s = stats.hmean([(TP/(TP+FP)),(TP/(TP+FN))])
    print(
    f'''
    _______________________________________________________________________________________
    
    True Positive = {TP} ---- False Positive = {FP}
    True Negative = {TN} ---- False Negative = {FN}
    
    Out of {TP+FN+FP+TN} predictions -- Correct predictions = {TP+TN} (True Pos + True Neg) 
    
    REAL POSITIVE = (TP + FN) = {TP+FN} ---- PREDICTED POSITIVE = (TP + FP) = {TP+FP}
    
    REAL NEGATIVE = (TN + FP) = {TN+FP} ---- PREDICTED NEGATIVE = (TN + FN) = {TN+FN}
     
        Accuracy = {acc:.2%} -->> Correct Predictions / Total Predictions
       Precision = {pre:.2%} -->> True Positive / Predicted Positive
             NPV = {NPV:.2%} -->> True Negative / Predicted Negative
          Recall = {rec:.2%} -->> True Positive / Real Positive
     Specificity = {spe:.2%} -->> True Negative / Real Negative
        f1-score = {f1s:.2%} -->> Harmonic Mean of Precision and Recall
    _______________________________________________________________________________________
    '''
    )

    
def random_forest_models(num_models, rand_st=123, positive=1, max_samp=1.0, trees=100):
    '''
    random_forest_models is a function that:
        
        Takes in:   num_models=  >> The number of rf models 
                                  you want to create  ;dtype(int)
                       rand_st=  >> Random State  
                                  ;dtype(int) = 123 unless specified
                      positive=  >> what is the positive test 
                                  (0 or 1)
                      max_samp=  >> maximum samples per tree
                                  ;dtype(int, float) = (default)1.0
                                  if int: = number of samples
                                  if float: = percentage of total samples
                         trees=  >> n_estimators: number of trees in the forest
        
Assumed variables apply:
    
                  train: training dataset
               validate: validate dataset
                   test: test dataset

                 X_cols = df.columns.drop('target_y').to_list()
                  y_col = 'target_y'

                X_train = train[X_cols]
                y_train = train[y_col]
                  X_val = validate[X_cols]
                  y_val = validate[y_col]
                 X_test = test[X_cols]
                 y_test = test[y_col]
                 
        Returns: a DataFrame with predictions for each model
    '''
    b = int(y_train.mode())
    preds = pd.DataFrame({
    'actual': y_train,
    'baseline': b,
    })
    depth = 11 #num_models * 2 + 1
#     fig, ax = plt.subplot(nrows = num_models,n)
    for i in range(1, num_models+1):
        depth -= 1
        name = f'model_{i}_depth_{depth}'
        
        rf = RandomForestClassifier(random_state = rand_st, 
                                    min_samples_leaf = i, 
                                    max_depth = depth,
                                    max_samples = max_samp,
                                    n_estimators = trees
                                   )
        rf.fit(X_train, y_train)
        
        preds[name] = rf.predict(X_train)
#         val_name = f'{name}_validate'
        TN, FP, FN, TP = confusion_matrix(preds.actual, preds[name]).ravel()
        print(f'\n{name}\n\n {rf}')
        confusion(TN=TN, TP=TP, FN=FN, FP=FP)
        print(f'Validation score is: {rf.score(X_val, y_val):.2%}')
        print('______________________________')
#         preds[val_name] = rf.predict(X_val)
#         plt.subplot(i,i,12)
#         plt.title(f'{name} feature importances')
#         plt.barh(X_train.columns, rf.feature_importances_)
#         plt.show
                
    return preds