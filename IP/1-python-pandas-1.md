# Python Pandas 1

- Types of storage in Pandas
  - **Series**: single type data
  - **Dataframe**: multiple type data
- These are methods to store similar kind of data.

> [!CAUTION] Write a python program to store the following sequence in a series. [10, 20, 30, 40]
>
> ```py
> import pandas as pd
> a = pd.series([10, 20, 30, 40]) 
> print(a)
> ```

> [!CAUTION] Write a python program to store the following sequence in a series. [e, x, a, m]
>
> ```python
> import pandas as pd
> a = pd.series(['e', 'x', 'a', 'm'])
> ```

- **Numpy** package is installed alongside pandas.


| Brace | Function |
| :-----: | :---------: |
|  []  | Only data |
|  {}  |   Index   |
|  ()  | Function |

- `pd.Series(np.linspace(10,100,20))`
  - Divide the numbers from 10 to 100 into 20 groups.
  - **Datatype**: float64
- `pd.Series(np.tile([10,100],20))`
  - Repeats 10 and 100 20 times each (40)
  - **Datatype**: int32
  - > [!NOTE]
    >
  - > Datatype is **float64** if values are given in decimals.
    >
- `pd.Series(100,index=["A", "B", "C"])`
  - Uses indexes A, B and C and gives them data 100
  - **Datatype**: int64
- `pd.Series(400,index=range(10,110,10))`
  - Prints from 10 to 100 index values skipping 10 values with data 400.
  - **Datatype**: int64
- `pd.Series({10:2,20:5,30:7})`
  - Uses indexes 10, 20 and 30 with the corresponding data.
  - **Datatype**: int64
- `pd.Series([70,80,np.NaN,100])`
  - Leaves an index in the middle for future input.
- `pd.Series(index=a,data=b)`
  - Imports list or set a and b into defined places.
- `np.arange(10,100)`
  - Prints range of 10 to 100 index numbers
- `pd.Series(np.arange(10,100))`
  - Serially arrange range 10 to 100 values into indexes.
  - Optionally, input `pd.Series(np.arange(10,100)*2)` or any other mathematical function to change the value of data.

# Dataframe


|         | Shop 1 | Shop 2 | Shop 3 | Shop 4 |
| :--------: | :------: | :------: | :------: | :------: |
| **1st year** |  50k  |  90k  |  35k  |  60k  |
| **2nd year** |  150k  |  250k  |  300k  |  45k  |
| **3rd year** |  290k  |  210k  |  350k  |  95k  |
| **4th year** |  20k  |  15k  |  10k  |  20k  |

- The below code prints the data in a data frame format.

```python
import pandas as pd 
a = [['50k', '90k', '35k', '60k'],['150k', '250k', '300k', '45k'],['290k', '210k', '350k', '95k'],[ '20k', '15k', '10k', '20k']]

s = pd.DataFrame(a,columns=['Shop 1', 'Shop 2', 'Shop 3', 'Shop 4'], index=['1st year', '2nd year', '3rd year', '4th year'])

print(s)
```

- `print(var.loc[<rowheader>:<rowheader>,<columnheader>:<columnheader>])`
  - From a dataframe, show the specific case-sensitive data. 
- `print(var.loc[<columnheader>])`
  - Print all rows with column data
- `print(var.loc[<rowheader>])`
  - Print all column data of a row. 
- `print(var.iloc[1:3,0:2])`
  - Prints data using address lines for row number and column respectively. 

<div style="page-break-after: always;"></div>

- `df["Hospital"] = (<values>)`
- `df.at[("<Indexname>")] = (<values>)`