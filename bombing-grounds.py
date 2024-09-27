import pandas as pd 
# import numpy as np 

a = [[7,6,6,8],[8,8,5,6],[7,6,6,9],[7,6,4,6]]

df = pd.DataFrame(a, index=("Andhra",'Odisha','MP','UP'), columns=('Toys','Books','Uniform','Shoes'))

print(df.loc['Andhra':'MP',:])