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

# Snippets
- `print(<dataframe_variable>.T)`
    - **T**: Transpose 
    - Swaps the places of Index and Column labels. 
- `print(<dataframe>[["column_label"]])`
    - Prints dataframe with only specified column and all index. 
- `print(df1.add(df2))`
    - Adds the tabular values of df1 and df2 and prints output. 
- `print(df.radd(df2))`
    - Does the same as above but use `df2 + df1` instead of `df1 + df2` 
- `print(df1.sub(df2))`
    - Subtract `df2` from `df1`
- `print(df1.rsub(df2))`
    - Subtract `df1` from `df2`
- `print(mul(df2))`
    - Multiply `df1` with `df2`
- `print(df1.div(df2))`
    - $\text{df}1 / \text{df}2$
- `print(df1.rdiv(df2))`
    - $\text{df}2 / \text{df}1$