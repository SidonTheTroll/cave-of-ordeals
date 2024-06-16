import pandas as pd

# Creating a sample DataFrame
data = {'A': [10, 20, 30], 'B': [5, 10, 15]}
i = ['A','B','C']
df = pd.DataFrame(data, index=i)

print(df)

print()

print(df['A'].unique())