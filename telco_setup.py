def telco_imports():
    '''
    imports the libraries im using in this environment
    '''
    print('''
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as m
from scipy import stats
from stat_tools import *
from sklearn.model_selection import train_test_split
import acquire
import prepare
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
# grab Decision Tree Classifier and some helping friends from sklearn.tree
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
# ignore warnings
import warnings
warnings.filterwarnings("ignore")
from modeling import confusion, random_forest_models
    ''')

def get_db_url(schema):
    import env
    user = env.username
    password = env.password
    host = env.host
    conn = f'mysql+pymysql://{user}:{password}@{host}/{schema}'
    return conn

def gdb(db_name, query):
    '''
    gdb(db_name, query):
    
        takes in    a (db_name) schema name from the codeup database ;dtype int
        and         a (query) to the MySQL server ;dtype int

        and         returns the query using pd.read_sql(query, url)
        having      created the url from my environment file
    '''
    from pandas import read_sql
    # from env import get_db_url
    url = get_db_url(db_name)
    return read_sql(query, url)


class Percent(float):
    def __str__(self):
        return '{:.2%}'.format(self)
    def __repr__(self):
        return '{:.2%}'.format(self)
    
