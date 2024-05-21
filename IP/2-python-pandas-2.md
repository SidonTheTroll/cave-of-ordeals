# Python Pandas 2

```py
import pandas as pd 
index = ['A','B']
s = {'English':[35,80],'Math':[70,80]}
df = pd.DataFrame(s)
print(df)
print()
for(row,rowSeries) in df.iterrows():
    print("RowIndex:",  row)
    print("Containing")
    print(rowSeries)
    print()
```

#### Output 
```
RowIndex: A
English: 35
Math: 70
Name: A, dtype: int64

RowIndex: B
English: 80
Math: 90
Name: B, dtype: int64
```

```py
import pandas as pd 
index = ['A','B']
s = {'English':[35,80],'Math':[70,80]}
df = pd.DataFrame(s)
print(df)
print()
for (column,ColumnSeries) in df.iteritems(): 
    print("Subject": column)
    print(ColumnSeries)
    print()
```

#### Output 
```
Subject: English 
A: 35 
B: 80 
Name: English, dtype: int64 

Subject: Math
A: 70
B: 90 
Name: Math, dtype: int64
```

# 22/05/24
- `print(<dataframe_variable>.T)`
    - **T**: Transpose 
    - Swaps the places of Index and Column labels. 