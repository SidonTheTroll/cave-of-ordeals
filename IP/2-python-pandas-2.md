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

## 3. Write the equivalent expressions 
1. A.add(B) = A + B 
2. B.add(A) = B + A 
3. A.sub(B) = A - B 
4. B.sub(A) = B - A 
5. A.rsub(B) = B - A 
6. B.mul(A) = B * A 
7. A.rdiv(B) = B / A 
8. B.div(A) = B / A 
9. B.rdiv(A) = A / B 
10. A.div(B) = A / B 

## 4. Is the results sub() and rsub() the same? Why/why not? 
No, the results aren't the same because the subtract the operands in different numbers. 

## 5. Write appropriate function to perform Dataframe. 
1. Calculate the sum = `sum()` 
2. Count the values = `count()`
3. Calculate the average = `mean()` 
4. Calculate the median = `median()` 
5. Calculate the mode = `mode()`
6. Calculate the standard deviation = `std()`
7. Calculate the variance = `var()`
8. Calculate the maximum value = `max()`

## 6. What does info() and describe() do? 
info() allows us to learn the shape of object types of our data. The describe() method gives us summary statistics for numerical column in our dataframe. 

## 7. Name some function that performs descriptive statistics in a dataframe. 
```py 
count()
median()
min()
max()
sum()
var()
quantile()
mean()
std()
```

## 8. Do sum() and add() functions the same? 
No, the sum() and add() function are not the same in pandas. The sum() functions calculates the sum of values along a specified axis while the add() function in pandas is used to add the object element wise. 

## 9. To consider only the numeric value for calculation, what argument do you pass the statistics function of pandas? 
`numeric_only=True` 

## 10. Is there one function that calculates much of descriptive statictics values? Name it. 
`describe()` 

## 11. What happens if mode() returns multiple values for a column but other columns have a single mode. 
If mode() returns multiple values for a column but other column have single mode then pandas will display 2 likes to show two modes and for the rest columns if fill NaN. 

## 12. What is quantile and quartile? 
Quantile are a set of three values that divide ordered datasets into four equal parts.  
While quartile are units of equal adjacent quantities in a distribution. 

## 13. Name the function you can use for filling missing data. 
`fillna()`

## 14. Name the function that you can calculate different types of quantities. 
`quantile()`

## 15. Name the function that gives you maximum and minimum values for a dataframe. 
`max()` and `min()`

## 16. Some questions but index of maximum and minimum values. 
`idxmax()` and `idxmin()`

## 17. What is missing data? 
These are placeholders that help us to input data after dataframe is created or finished. 

## 18. Why is missing data filled in dataframe with same values? 
Because empty value cannot be displayed by Nan. There may be more than one mode for a dataframe. 