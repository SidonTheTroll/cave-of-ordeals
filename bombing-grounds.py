import pandas as pd

ser = pd.Series(range(41, 71, 3))
for i in range(0, ser. size):
    if ser[i] % 2 == 0:
        ser[i] = ser[i]-3
    elif ser[i] % 2 != 0:
        ser[i] = ser[i]+7

print(ser)
