import pandas as pd
numbers = []

for i in range(1, 11):
    val = int(input("Enter a number: "))
    numbers.append(val)
ser = pd.Series(numbers)

ser[ser % 4 == 0] = 0
print(ser)
