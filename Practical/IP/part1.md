# Part 1: Data Handling using Pandas 
## 1. Create a series of these numbers: 33, 55, 65,29, 19, 23. Find the sum of those values which are ending with 3 or 5. 
```python
import pandas as pd 

list = [33, 55, 65,29, 19, 23]
ser = pd.Series(list)

sum5 = sum(ser[ser % 10 == 5])
sum3 = sum(ser[ser % 10 == 3])

print("Sum of mod 5:", sum5)
print("Sum of mod 3:", sum3)
print("Sum of both together:", sum5+sum3)
```

## 2. Create a series of 10 numbers starting with 41 and with the increment of 3. Now add 7 to all odd values and subtract 3 in even values. Reprint the updated series. 
```python
import pandas as pd

ser = pd.Series(range(41,71,3))

for i in range(0,ser.size):
    if ser[i] % 2 == 0:
        ser[i] = ser[i]-3
    else:
        ser[i] = ser[i] + 7

print(ser)
```

## 3. Create a series of 10 numbers. Change the value of all the elements those values are multiples of 4. 
```python
import pandas as pd
numbers = []

for i in range(1,11):
    val = int(input("Enter a number: "))
    numbers.append(val)
ser = pd.Series(numbers)

change = int(input("Assign the number of multiples of 4: "))

ser[ser % 4 == 0] = change
paint(ser)
```

## 4. Create a series and print the top 3 elements using the head function. 
```python
import pandas as pd

ser_length = int(input("Enter the length of the series: "))
data = []

for i in range(ser_length):
    val = int(input("Enter a value: "))
    data.append(val)

ser = pd.Series(data)
print(ser.head(3))
```

## 5. Create a series and print the bottom 3 elements using the tail function. 
```python
import pandas as pd

ser_length = int(input("Enter the length of the series: "))
data = []

for i in range(ser_length):
    val = int(input("Enter a value: "))
    data.append(val)

ser = pd.Series(data)
print(ser.tail(3))
```

## 6. Create a series witht these numbers: 21, 51, 71, 31, 12. Exchange all these values of series by shifting each of them on to one position before and by shifting the first value to last position. 
```python
import pandas as pd 
import numpy as np 

s = pd.Series([21,51,71,31,12])
print(pd.Series(np.roll(s.values, -1), index = s.index))
```

## 7. Create a dataframe named as students using a list of name of 5 students. 
```python
import pandas as pd 

students = ["A","B","C","D","E"]
students = pd.DataFrame(students,columns=["Name"])

print(students)
```

## 8. Create a dataframe players using a list of names and scores of the previous three matches (using nested list).
```python
import pandas as pd 

data = [["A",55,66,31],["B",88,66,43],["C",99,85,68]]
players = pd.DataFrame(data, columns = ["Name","M1","M2","M3"])

print(players)
```

## 9. Create a dataframe `countries` using a dictionary which stores country name, capitals and populations of the country. 
```py 
import pandas as pd

country_data = {"Country Name": ["India", "Canada", "Australia"], "Capital": ["New Delhi", "Ottawa", "Canberra"], "Population": ["136 Cr", "10 Cr", "50 Cr"]}
countries = pd.DataFrame(country_data)

print(countries)
```

## 10. Iterate dataframe created in question no. 8 by its rows. 
```python
import pandas as pd

data = [["A", 55, 66, 31], ["B", 88, 66, 43], ["C", 99, 85, 68]]
players = pd.DataFrame(data, columns=["Name", "Match-1", "Match-2", "Match-3"])

for index, row in players.iterrows():
    print(index, row.values)
```

## 11. Print scores of previous two matches along with their names using iterrows function (use dataframe created in question 8). 
```python
import pandas as pd

data = [["A", 55, 66, 31], ["B", 88, 66, 43], ["C", 99, 85, 68]]
players = pd.DataFrame(data, columns=["Name", "Match-1", "Match-2", "Match-3"])

for index, row in players.iterrows():
    print(index, row["Name"], row["Match-1"], row["Match-2"], row["Match-3"])
```

## 12. Make a total of score from the dataframe players and display their rank according to their scores. 
```python
import pandas as pd

data = [["A", 55, 66, 31], ["B", 88, 66, 43], ["C", 99, 85, 68]]
players = pd.DataFrame(data, columns=["Name", "Match-1", "Match-2", "Match-3"])

players["Total_Score"] = players["Match-1"] + players["Match-2"] + players["Match-3"]
players["Rank"] = players["Total_Score"].rank(ascending=False)

print(players)
```

## 13. Print the batsman name along with the runs scored in Test and T20 using column names and dot notation. 
```python 
import pandas as pd

player_data = {"Name": ["A", "B", "C", "D", "E"], "Test": [3543, 2578, 2280, 2158, 1879], "ODI": [2245, 2165, 2080, 1957, 1856], "T20": [1925, 1853, 1522, 1020, 980]}

data = pd.DataFrame(player_data)

data.index = data.index + 1

print(data.Name)
print("=========================================")
print("Test Record:")
print(data.Test)
print("=========================================")
print("T20 Record:")
print(data.T20)
```

## 14. Display the batsman name along with runs scored in ODI using `loc`.
```python
import pandas as pd

player_data = {"Name": ["A", "B", "C", "D", "E"], "Test": [3543, 2578, 2280, 2158, 1879], "ODI": [2245, 2165, 2080, 1957, 1856], "T20": [1925, 1853, 1522, 1020, 980]}

data = pd.DataFrame(player_data)

data.index += 1

print(data.loc[:, ("Name", "ODI")])
```
