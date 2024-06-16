import pandas as pd

A = [[10,20,30,40,50,60,70,80,90,100]]

data = pd.DataFrame(A, index=['A'], columns=['A','B','C','D','E','F','G','H','I','J'])

print(data)
print()

print(data.median(axis=1))