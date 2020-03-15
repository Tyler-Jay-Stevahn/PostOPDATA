from django_pandas.managers import DataFrameManager
import pandas as pd
from .models import employees
import psycopg2
from sqlalchemy import create_engine

def to_dataframe(new_info):
    alchemyengine = create_engine('postgres://njmivolvyzlzuy:57ae5bd78a1465930c9db72346af6228ee31d9328cb5a76ac29d6c4c485f007a@ec2-18-213-176-229.compute-1.amazonaws.com:5432/d13p0g0bkpor3r')
    dbConnection = alchemyengine.connect();

    data = pd.read_sql("select * from \"database_test_employees\"", dbConnection);
    print(data.head(1))
