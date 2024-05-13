import pandas as pd 
import numpy as np

stu = {'A':39,'B':41,'C':42,'D':43,'E':44,'F':45}

s = pd.Series(stu)

s.index.name = "OK"

print(s)