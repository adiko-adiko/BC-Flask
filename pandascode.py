import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://sha2user:Boot!camp2021!@localhost/adoption')

df = pd.read_csv('puppy.csv')
df2 = pd.read_csv('owner.csv')

df2.to_sql(
    name='listofowners',
    con=engine,
    index=False,
    if_exists='append'
)

df.to_sql(
    name='listofpuppies',
    con=engine,
    if_exists= 'append', 
    index=False
)

#Counts per table
df.count()

#Number of columns
colmns = df.columns
print("Number of columns: ", len(colmns))

col = df2.columns
print("Number of columns: ", len(col))

#group by
grb = df.groupby('name')['spots'].count()