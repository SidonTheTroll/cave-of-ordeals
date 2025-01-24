import pandas as pd

player_data = {"Name": ["A", "B", "C", "D", "E"], "Test": [3543, 2578, 2280, 2158, 1879], "ODI": [2245, 2165, 2080, 1957, 1856], "T20": [1925, 1853, 1522, 1020, 980]}

data = pd.DataFrame(player_data)

data.index += 1

print(data.loc[:, ("Name", "ODI")])
