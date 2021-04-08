import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://sha2user:Boot!camp2021!@localhost/adoption')

df = pd.read_csv('puppy.csv')

df.to_sql(
    name='ListofPuppies',
    con=engine,
    set_index('ID')
)
df2 = pd.read_csv('owner.csv')

df2.to_sql(
    name='ListofOwners',
    con=engine,
    set_index('ID')
)

#Counts per table
df.count()

#Number of columns
colmns = df.columns
col = df2.columns
print("Number of columns: ", len(colmns))
print("Number of columns: ", len(col))

#group by
grb = df.groupby('name')['spots'].count()