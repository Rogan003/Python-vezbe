from sqlalchemy import create_engine
import pymysql
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

db_connection_str = 'mysql+pymysql://root:malivesa003@localhost/balanspalacinke'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM balapp_prodaja', con=db_connection)
print(df['brojPalacinaka'])
print(df)

plt.plot(df['godina'],df['brojPalacinaka'])
plt.show()

nesto = input()