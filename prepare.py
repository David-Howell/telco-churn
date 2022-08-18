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

    encode = ['partner', 'dependents', 'phone_service', 'internet_service_type', 
             'contract_type', 'paperless_billing', 'payment_type', 'churn']
    
    combine = ['online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']

    df['null_charges'] = pd.to_numeric(df['total_charges'], errors='coerce').isnull()

    df['total_charges'][df['null_charges'] == True] = df['monthly_charges'][df['null_charges'] == True]

    df.total_charges = df.total_charges.astype(float)

    df.drop(columns= ['null_charges', 'gender', 'multiple_lines'], inplace=True)

    dummy_df = pd.get_dummies(df[encode], drop_first=True)

    df = pd.concat([df, dummy_df], axis=1)

    df = df.drop(columns=encode)
    print(df.info())
    return df


def split_data(df, strat_by, rand_st=123):
    '''
    Takes in: a pd.DataFrame()
          and a column to stratify by  ;dtype(str)
          and a random state           ;if no random state is specifed defaults to [123]
          
      return: train, validate, test    ;subset dataframes
    '''
    train, test = train_test_split(df, test_size=.2, 
                               random_state=rand_st, stratify=df[strat_by])
    train, validate = train_test_split(train, test_size=.25, 
                 random_state=rand_st, stratify=train[strat_by])
    print(f'Prepared df: {df.shape}')
    print()
    print(f'Train: {train.shape}')
    print(f'Validate: {validate.shape}')
    print(f'Test: {test.shape}')


    return train, validate, test