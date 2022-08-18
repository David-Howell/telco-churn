from telco_setup import gdb
import os
import pandas as pd

def get_telco_data():
    filename = "telco_churn.csv"
    
    # if telco_churn.csv is saved locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if telco_churn.csv is not saved locally, acquire data from codeup MySQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df = gdb('telco_churn', 
                '''
                SELECT c.customer_id, c.gender, c.senior_citizen, c.partner, c.dependents, c.tenure, c.phone_service, c.multiple_lines,
			ist.internet_service_type, c.online_security, c.online_backup, c.device_protection,
            c.tech_support, c.streaming_tv, c.streaming_movies, ct.contract_type, c.paperless_billing,
            pt.payment_type, c.monthly_charges, c.total_charges, c.churn
        
        FROM customers c
			JOIN internet_service_types ist
				ON c.internet_service_type_id = ist.internet_service_type_id
			JOIN contract_types ct
				ON c.contract_type_id = ct.contract_type_id
			JOIN payment_types pt
				ON c.payment_type_id = pt.payment_type_id;      
                ''')
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)

        # Return the dataframe to the calling code
        return df  
