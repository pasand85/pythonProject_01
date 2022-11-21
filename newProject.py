

# LetterCount
import numpy as np
import pandas as pd

data = {
    "students": ['Emma', 'John', np.nan, 'Bob'],
    "grades": [12, np.nan, 18, 17]
}
df =  pd.DataFrame(data) #,index=['a','b','c'])

df['students'].fillna('No Name',inplace = True)
df['grades'].fillna('No Grade',inplace = True)
#f_row = df.loc['a']
df2 = df.replace('Emma','Andreas')
#print(f_row)
for i,j in df2.iterrows():
    print(i,j)
    print()
dfcol = list(df)
for i in dfcol:
    print(dfcol[i][1])


L = [5, 10, 15, 20, 25]
ds = pd.Series(L)
print(ds)
print(' - - - - - -')
d = {'col1': [1, 2, 3, 4, 7, 11],
       'col2': [4, 5, 6, 9, 5, 0],
       'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(d)
newS = df.iloc[:,0]
print('First Column as Series: ')
print(newS)
print(type(newS))
print(' - - - - - -')

