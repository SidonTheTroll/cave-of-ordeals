# Part 1: Data Handling using Pandas 
1. Create a series of these numbers: 33, 55, 65,29, 19, 23. Find the sum of those values which are ending with 3 or 5. 

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

2. Create a series of 10 numbers starting with 41 and with the increment of 3. Now add 7 to all odd values and subtract 3 in even values. Reprint the updated series. 

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

3. Create a series of 10 numbers. Change the value of all the elements those values are multiples of 4. 

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

4. Create a series and print the top 3 elements using the head function. 

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

5. Create a series and print the bottom 3 elements using the tail function. 

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

6. Create a series witht these numbers: 21, 51, 71, 31, 12. Exchange all these values of series by shifting each of them on to one position before and by shifting the first value to last position. 

```python
import pandas as pd 
import numpy as np 

s = pd.Series([21,51,71,31,12])
print(pd.Series(np.roll(s.values, -1), index = s.index))
```