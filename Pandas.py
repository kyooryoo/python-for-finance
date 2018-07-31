import numpy as np
import pandas as pd

from os import chdir, getcwd
chdir('/Users/user/Downloads/python-for-finance-and-trading-algorithms/python-for-finance')
getcwd()

# Series has axis labels, can be indexed by a label, can hold Python objects
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([110,120,130])
d = {'aa':210,'bb':220,'cc':230}
d2 = {'aa':[110,120,130],'bb':[210,220,230],'cc':[310,320,330]}

# create series
# pd.Series(data,index)
pd.Series(data=my_list)
pd.Series(labels)
pd.Series(index=labels,data=my_list)
pd.Series(arr)
pd.Series(labels,arr)
pd.Series(d)
pd.Series(d2)
pd.Series([sum,print,len])

ser1 = pd.Series([1,2,3,4],['a','b','c','d'])
ser1
ser2 = pd.Series([1,3,4,5],['a','c','d','e'])
ser2

ser1['c']
ser1 + ser2
ser1 - ser2
ser1 * ser2
ser1 / ser2

# create DataFrame
from numpy.random import randn
df = pd.DataFrame(d2)
df
np.random.seed(101)
df = pd.DataFrame(data=randn(5,4),index=['A','B','C','D','E'],columns='W X Y Z'.split())
df
# iterative way
df = pd.DataFrame(data=randn(5,4))
df.index = ['A','B','C','D','E']
df.columns = 'W X Y Z'.split()
# select column
df['W']
df[['W','Z']]
# select row
df.loc['A']
df.iloc[2]
df.loc[['A','C']]
df.iloc[[0,2]]
df[[True,False,True,False]]
# select special items
df['Y']['B']
df.loc['B','Y']
df.loc[['B','E'],['X','Y']]
df.loc[['A','E'],['W','Z']]
# SQL Syntax for selecting a column
df.X # not recommended
# create a new column
df['NEW'] = df['X'] + df['Y']
df
# default drop is not inplace
df.drop('NEW',axis=1)
df
# specify inplace drop
df.drop('NEW',axis=1,inplace=True)
df
# drop rows
df.drop('C',axis=0)
df
df.drop('D',axis=0,inplace=True)
df
# conditional selection
df # original dataframe
df>0 # convert to a boolean dataframe
df[df>0] # use a boolean dataframe as input for selection
# select all items with values on column W > 0
# delete rows with values on column W <=0
df[df['W']>0]
df[df['W']>0]['Y']
df[df['W']>0][['Y','X','Z']]
df[(df['W']>0) & (df['Y']>0)]
# reset index to integer sequence, put original index to new column 'index'
df.reset_index(inplace=True)
df
# index could be further modified
df.index='A B C D E'.split()
df
# when 'index' column already exists, original index will be put in 'level_0'
df.reset_index(inplace=True)
df
df.drop('level_0',axis=1,inplace=True)
df
# reset index to a specific one with the column name on top
df.set_index('index',inplace=True)
df
# multi-level index
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
# grap items with multi-level index
df.loc['G1']
df.loc['G1'].loc[2]
# alternative way
df.xs('G1')
df.xs(['G1',2])
df.xs(1,level='NUM')
df.xs('G2',level='GROUP')
# name the multi index
df.index.names
df.index.names = ['GROUP','NUM']
df

# processing missing data
df = pd.DataFrame({'A':[1,2,3],'B':[4,np.nan,np.nan],'C':[7,8,np.NaN]})
df
# drop rows with NaN data
df.dropna()
# drop columns with NaN data
df.dropna(axis=1)
# drop row with two NaN data
df.dropna(thresh=2)
# replace NaN with a value
df.fillna(value='FILL VALUE')
df.fillna(value=23)
# replace nan with mean of the column
for col in df.columns:
    df[col].fillna(value=df[col].mean(),inplace=True)
df

# groupby groups rows of data and call aggregate functions
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
data
df = pd.DataFrame(data)
df
# create a groupby object
df.groupby('Company')
by_comp = df.groupby('Company')
by_comp.mean()
df.groupby('Company').std()
by_comp.min()
by_comp.max()
by_comp.count()
by_comp.describe()
by_comp.describe().loc['GOOG']
by_comp.describe().transpose()
by_comp.describe().transpose()['MSFT']

# merging joining and concatenating
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
df22 = pd.DataFrame({'E': ['A4', 'A5', 'A6', 'A7'],
                        'F': ['B4', 'B5', 'B6', 'B7'],
                        'G': ['C4', 'C5', 'C6', 'C7'],
                        'H': ['D4', 'D5', 'D6', 'D7']},
                         index=[0, 1, 2, 3])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
pd.concat([df1,df2,df3])
pd.concat([df1,df2,df3],axis=1)
pd.concat([df1,df22],axis=1)
pd.concat([df1,df22])

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})
left
right
pd.merge(left,right,on='key')

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})
left
right
# merge rows that have the same combination of key1 and key2
pd.merge(left,right,on=['key1','key2'])
pd.merge(left,right,on=['key1','key2'],how='outer')
pd.merge(left,right,on=['key1','key2'],how='right')
pd.merge(left,right,on=['key1','key2'],how='left')


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
left
right
left.join(right)
left.join(right,how='outer')
right.join(left)
right.join(left,how='outer')
left.join(right,how='inner')
left.join(right,how='right')
right.join(left,how='right')

# operations
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df
df.head(2)
df.tail(2)

df['col2'].unique()
df['col2'].nunique()
df['col2'].value_counts()

df['col1']>2
df[df['col1']>2]
df[(df['col1']>2) & (df['col2']==444)]

def times2(x):
    return x*2
df['col1'].apply(times2)
df['col3'].apply(len)
df['col2'].sum()

del df['col1']
df

df.columns
df.index

df.sort_values(by='col3')
df.sort_values('col2')

df.loc[3,'col3']=np.NaN
df
df.isnull()
df.dropna()
df.fillna('WasNaN')

df = pd.DataFrame(
        {'A':['CN','CN','CN','JP','JP','JP'],
         'B':['MS','MS','FB','FB','MS','MS'],
         'C':['F','M','F','M','F','M'],
         'D':[1,3,2,5,4,1]})
df
df.pivot_table(values='D',index=['A','B'],columns=['C'])

# data input and output
df.to_csv('example.csv',index=False)
pd.read_csv('example.csv')

df.to_excel('Excel_Sample.xlsx',sheet_name='sheet1')
pd.read_excel('Excel_sample.xlsx')

df = pd.read_html('https://www.state.nj.us/dobi/bankwebinfo.htm')
df[0]
df[1][0].iloc[1:6]

# Exercise
# read in the banklist.csv file into a dataframe
df = pd.read_csv('banklist.csv')
# Show the head of the dataframe, columns
df.head()
df.columns
# How many States (ST) are represented in this data set?
df['ST'].nunique()
df['ST'].unique()
# the top 5 states with the most failed banks
df.groupby('ST').count().sort_values('City',ascending=False)['City'].head(5)
df['ST'].value_counts().head(5)
# What are the top 5 acquiring institutions?
df['Acquiring Institution'].value_counts().iloc[:5]
# banks has the State Bank of Texas acquired, actually in Texas?
df[df['Acquiring Institution']=='State Bank of Texas']
df[(df['Acquiring Institution']=='State Bank of Texas')&(df['ST']=='TX')]
# What is the most common city in California for a bank to fail in?
df[df['ST']=='CA']
df[df['ST']=='CA'].groupby('City').count()
df[df['ST']=='CA'].groupby('City').count().sort_values('Bank Name',ascending=False)
df[df['ST']=='CA'].groupby('City').count().sort_values('Bank Name',ascending=False).head(1)
df[df['ST']=='CA'].groupby('City').count().sort_values('Bank Name',ascending=False).head(1)['Bank Name']
# How many failed banks don't have the word "Bank" in their name?
df['Bank Name'].apply(lambda name: 'Bank' not in name)
df['Bank Name'].apply(lambda name: 'Bank' not in name).value_counts()
sum(df['Bank Name'].apply(lambda name: 'Bank' not in name))
# How many bank names start with the letter 's' ?
sum(df['Bank Name'].apply(lambda name: name[0].upper() =='S'))
# How many CERT values are above 20000 ?
sum(df['CERT']>20000)
# How many bank names consist of just two words? (e.g. "First Bank" , "Bank Georgia" )
sum(df['Bank Name'].apply(lambda name: len(name.split())==2))
# How many banks closed in the year 2008?
sum(df['Closing Date'].apply(lambda date: date[-2:]) == '08')
pd.to_datetime(df['Closing Date'])
sum(pd.to_datetime(df['Closing Date']).apply(lambda date: date.year) == 2008)




