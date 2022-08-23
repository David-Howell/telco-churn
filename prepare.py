import acquire
import pandas as pd
from sklearn.model_selection import train_test_split


def prep_telco():
    '''
    Uses the local acquire.py to get the telco_churn data 
    from local .csv or codeup MySQL DB if not locally available.
    
    Encodes Yes/No data into 1/0 data from the following collumns:
    
                    partner
                    dependents
                    phone_service
                    internet_service_type
                    contract_type
                    paperless_billing
                    payment_type
                    churn
                    
    Combines the following columns to reflect the number of 
    extra services for each customer:
    
                    online_security
                    online_backup
                    device_protection
                    tech_support
                    streaming_tv
                    streaming_movies
                    
    Tracks the null charges in `total_charges` associated with 
    new accounts and transfers over the customer's `monthly_charges`
    
    Drops extraneous or confounding columns
    
    --------------------------
    No Parameters nescesary:
    --------------------------
    
    prints the .info() for the resulting DataFrame
    
    returns a pd.DataFrame
    '''
    df = acquire.get_telco_data()
# set the columns to be encoded
    encode = ['partner', 'dependents', 'phone_service', 'internet_service_type', 
             'contract_type', 'paperless_billing', 'payment_type', 'churn']
#     set the columns to be combined
    combine = ['online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
# make a boolean mask showing True for nulls in total_charges
    df['null_charges'] = pd.to_numeric(df['total_charges'], errors='coerce').isnull()
# The following line needs to be fixed in a future version using .loc[] notation
#     carries over the monthly charges to the total charges where total charges was null
#         This makes sense because the tenure was also 0 meaning these were new customers
    df['total_charges'][df['null_charges'] == True] = df['monthly_charges'][df['null_charges'] == True]
#     re-type the total_charges column to be all float
    df.total_charges = df.total_charges.astype(float)
#     drop the mask(null_charges), gender(not a factor to be explored), multiple_lines(confounding with DSL+Phone)
    df.drop(columns= ['null_charges', 'gender', 'multiple_lines'], inplace=True)
#     encode the columns to be encoded
    dummy_df = pd.get_dummies(df[encode], drop_first=True)
#     add the encoded columns to the dataframe
    df = pd.concat([df, dummy_df], axis=1)
#     drop the columns that were encoded
    df = df.drop(columns=encode)
#     print the resultant DataFrame's .info()
    print(df.info())
    return df

def split_data(df, strat_by, rand_st=123):
    '''
    Takes in: a `pd.DataFrame()`
          and a `column` to stratify by  ;dtype(str)
          and a `random state`           ;if no random state is specifed defaults to [123]
          
      prints the `.shape` of the `DataFrame` taken in and the
      `Train`, `Validate`, and `Test` `DataFrames` returned
      `return: train, validate, test`    ;subset `DataFframes`
    '''
#     train test split giving 20% to the testing data set and stratifying by the Parameter field: strat_by
    train, test = train_test_split(df, test_size=.2, 
                               random_state=rand_st, stratify=df[strat_by])
#     train test split to break out a validation set the same size as the test set
    train, validate = train_test_split(train, test_size=.25, 
                 random_state=rand_st, stratify=train[strat_by])
#     print the name and shape of the resultant DataFrames
    print(f'Prepared df: {df.shape}')
    print()
    print(f'Train: {train.shape}')
    print(f'Validate: {validate.shape}')
    print(f'Test: {test.shape}')

#     returns the resulting DataFrames in order of train, validate, test 
    return train, validate, test


def split_data_model(df, strat_by, rand_st=123):
    '''
    Takes in: a `pd.DataFrame()`
          and a `column` to stratify by  ;dtype(str)
          and a `random state`           ;if no random state is specifed defaults to [123]
          
      prints the `.shape` of the `DataFrame` taken in and the
      `Train`, `Validate`, and `Test` `DataFrames` returned
      `return: train, validate, test`    ;subset `DataFframes`
    '''
#     train test split giving 20% to the testing data set and stratifying by the Parameter field: strat_by
    train, test = train_test_split(df, test_size=.2, 
                               random_state=rand_st, stratify=df[strat_by])
#     train test split to break out a validation set the same size as the test set
    train, validate = train_test_split(train, test_size=.25, 
                 random_state=rand_st, stratify=train[strat_by])
#     Remove extraneous training data:
    # get the index of the one year contract drops
    one_year_drops = train[(train.one_year == 1)&(train.tenure < 13)].index
    # get the index of the two year contract drops
    two_year_drops = train[(train.two_year == 1)&(train.tenure < 25)].index
    # cast both.tolist() and addd them together to have an index to drop from train
    contract_drops = one_year_drops.tolist()+two_year_drops.tolist()
    train.drop(index=contract_drops, inplace=True)

#     print the name and shape of the resultant DataFrames
    print(f'Prepared df: {df.shape}')
    print()
    print(f'Train: {train.shape}')
    print(f'Validate: {validate.shape}')
    print(f'Test: {test.shape}')

#     returns the resulting DataFrames in order of train, validate, test 
    return train, validate, test

def fix_nulls():
    df = acquire.get_telco_data()
#     drop_columns = ['gender', 'phone_service', 'multiple_lines', 'streaming_tv', 'streaming_movies']
    df.total_charges = pd.to_numeric(df.total_charges, errors='coerce')
    df['null_charges'] = pd.to_numeric(df['total_charges'], errors='coerce').isnull()

    df['total_charges'][df['null_charges'] == True] = df['monthly_charges'][df['null_charges'] == True]
    return df


def prep_telco_1(train):
    train['churn1'] = train.churn == "Yes"
    train['churn1'] = train['churn1'].map({False: 0, True:1})
    
    # copy paste and fix the typo
    drop_columns = ['gender',
     'phone_service',
     'multiple_lines',
     'streaming_tv',
     'streaming_movies',
     'churn',
     'null_charges',
     'customer_id']
    train.drop(columns=drop_columns, inplace=True)
    for i in train[['partner', 'dependents', 
       'online_security', 
       'online_backup', 
       'device_protection', 
       'tech_support', 
       'paperless_billing']]:
        train[i] = train[i].map({'Yes': 1, 'No': 0, 'No internet service': 0})
    dummy_list = ['internet_service_type', 'contract_type', 'payment_type']
    dummies = pd.get_dummies(train[dummy_list])
    train = pd.concat([train, dummies], axis=1)
    train['add_ons'] = train.online_backup + train.online_security + train.device_protection + train.tech_support
    drop_dummies = ['internet_service_type', 
               'online_security', 
               'online_backup', 
               'device_protection', 
               'tech_support',
               'contract_type',
               'payment_type',
               'internet_service_type_None',
               'contract_type_Month-to-month',
               'payment_type_Mailed check'
              ]
    train.drop(columns=drop_dummies, inplace=True)
    train.columns = ['senior', 'partner', 'dependents', 'tenure',
       'e_bill', 'monthly_charges', 'total_charges', 'churn1',
       'DSL', 'Fiber',
       'one_year', 'two_year',
       'bank_transfer',
       'cc', 'e_check',
       'add_ons']
    return train
    