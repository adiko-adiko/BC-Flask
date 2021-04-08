import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://sha2user:Boot!camp2021!@localhost/adoption')


df = pd.read_csv('puppy.csv')
df2 = pd.read_csv('owner.csv')

#reading the csv of the owner table
df2.to_sql(
    name='listofowners',
    con=engine,
    index=False,
    if_exists='append'
)

#reading the csv of the puppies table
df.to_sql(
    name='listofpuppies',
    con=engine,
    if_exists= 'append', 
    index=False
)

#Counts per table for puppies table
df.count()

#Counts per table for owner table
df2.count()

#Number of columns for puppies table
colmns = df.columns
print("Number of columns: ", len(colmns))

#Number of columns for the owner table
col = df2.columns
print("Number of columns: ", len(col))

#count of how many puppies have the given number of spots
grb = df.groupby(['Spots'])['Name'].count()
print(grb)