import pandas as pd

ser = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

ser.name = 'newInd'

print(ser)
