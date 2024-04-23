import pandas as pd 
a = [['50k', '90k', '35k', '60k'],['150k', '250k', '300k', '45k'],['290k', '210k', '350k', '95k'],[ '20k', '15k', '10k', '20k']]

s = pd.DataFrame(a,columns=['Shop 1', 'Shop 2', 'Shop 3', 'Shop 4'], index=['1st year', '2nd year', '3rd year', '4th year'])

print(s)