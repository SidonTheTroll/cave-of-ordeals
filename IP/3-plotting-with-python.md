# Plotting with Python 

- **Package**: matplotlib.pyplot 

- **Graphs possible**: 
    1. **Line chart**: `plot()`
    2. **Gar graph**: `bar()` or `barh()`
    3. **Scatter plot**: `scatter()`
    4. **Pie chart**: `pie()`
    5. **Histogram**: `hist()`
    6. **Boxplot chart**: `boxplot()`

```py 
import matplotlib.pyplot as pp 
week = [1,2,3,4]
prices = [30,25,32,40]

pp.plot(weight,prices,color='red') # Color isn't necessary but can be given manually

pp.grid(True) # Prints the output in a grid
pp.show()
```