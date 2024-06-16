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
- `print(df.min())`
    - Prints the minimum value of each column. Axis applicable
- `print(df.max())`
    - Prints the maximum value of each column. Axis applicable
- `print(df.mode(axis=0))`
    - Prints the value that appears the most in a column 
- `print(df.mean())`
    - Finds the mean (average) of a column in a data frame.
- `print(df.median)`
    - Returns (prints) the middle number in a set of numbers.
- `print(round(df.sum(axis=1))/3)`
    - First adds the row data in a data frame and divides it by 3 and them rounds them off to the ones place. 
- `print(df.quantile([0.25,0.50,0.75,1.0], axis=1))`
    - From a set of numbers in a data frame, calculate the distribution of numbers and find the specific values that fit the ratio in the set. 
- `print(df.describe())`
    - Describes all the attributes in a data frame in the following sections: count, mean, std, min, 25%, 50%, 75% and max. 
    - For a string-type data frame, it will give the following sections: count, unique, top and freq.


# QnA 

## 1. Name the function to iterate over a DataFrame horizontally. 
`<dataframe_object>.iterrows()`

## 2. Name the function to iterate over a DataFrame vertically. 
`<dataframe_object>.iteritems()`

## 3. Is the result of sub() and rsub() the same? Why/why not?
The results are different because subtraction gives 2 different answers based on the position of numbers while calculation. 

## 4. Write appropriate functions to perform the following on a DataFrame ?
1. Calculate the sum: `df1.sum(df2)`
2. Count the values: `df['values'].value_counts()`
3. Calculate the average: `df.mean()`
4. Calculate the most repeated value: `df.mode()`
5. Calculate the median: `df.median(axis=0)`
6. Calculate the standard deviation: 
7. Calculate the variance:
8. Calculate the maximum value:
9. Calculate the standard deviation:
10. Calculate the variance:

## 6. What does info() and describe() do?

## 7. Are sum() and add() functions the same?
No, they are not the same. `sum()` functions calculate the sum of elements in an iterable while `add()` deals with dataframe and ndarray objects.

## 8. Name some functions that perform descriptive statistics on a DataFrame.

## 9. To consider only the numeric values for calculation, what argument do you pass to statistics functions of Pandas?

## 10. Is there one function that calculates much of descriptive statistics values? Name it.

## 11. What happens if mode() returns multiple values for a column but other columns have a single mode?

## 12. What is quantile and quartile?

## 13. Name the function that lets you calculate different types of quantiles.

## 14. Name the functions that give you maximum and minimum values in a DataFrame.
For maximum, use `max()` and use `min`()` to find the minimum value. 

## 15. Name the functions that give you the index of maximum and minimum values in a DataFrame.
- Maximum: `idxmax()`
- Minimum: `idxmin()`

## 16. What is pivoting? Name the two functions that you can use for pivoting.

## 17. What is the basic difference between pivot() and pivot_table()?

## 18. What is missing data?
Missing data are special markers in python which deals with common data analysis and processing and reserves spaces for numbers to be inputted in the future

## 19. Why is missing data filled in DataFrame with some value?
Is is done so that the dataset is complete before entering the data in the future. 

## 20. Name the functions you can use for filing missing data. 

## 21. Name the function to create a histogram from a DataFrame. 

## 22. Name some functions used to handle missing data in DataFrames. 

## 23. Name some functions used to join or combine DataFrames. 

## 24. Name two functions that can produce result similar to SQL joins. 