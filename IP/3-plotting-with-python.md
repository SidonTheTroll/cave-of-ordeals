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

# Changing Line Color and Style 
## Changing Colors 
`matplotlib.pyplot.plot(<data1>,<data2>,<colorcode>)`

| <center> **Color** | <center> **Character** | 
|-|-| 
| Blue | b | 
| Green | g | 
| Red | r | 
| Magenta | m | 
| Yellow | y | 
| Black | k | 
| Cyan | c | 
| White | w | 

## Changing Line Style
`matplotlib.pyplot.plot(<data1>,<data2>,linestyle=<linecode>)`

| <center> **Code** | <center> Pattern | 
| `:` | Dotted | 
| `-.` | Dash-dot | 
| `--` | Dashed | 
| `-` | Solid | 

## Changing Marker Style 
`matplotlib.pytplot.plot(<data1>,<data2>,<colorcode>,marker='<markercode>',markersize=<num_value>,markeredgecolor='<colorcode>')`

| <center> **Marker** | <center> **Description** | 
|-|-|
| `.` | Point marker | 
| `,` | Pixel marker | 
| `o` | Circle marker | 
| `+` | Plus marker | 
| `x` | x marker | 
| `D` | Diamond marker | 
| `d` | Thin diamond marker | 
| `s` | Square marker | 
| `p` | Pentagon marker |
| `*` | Star marker | 
| `h` | Hexagon1 marker | 
| `H` | Hexagon2 marker | 
| `1` | Tri-down marker | 
| `2` | Tri-up marker | 
| `3` | Tri-left marker | 
| `4` | Tri-right marker | 
| `v` | Triangle-down marker | 
| `^` | Triangle-up marker | 
| `<` | Triangle-left marker | 
| `>` | Triangle-right marker | 
| `\|` | Vertile-line marker | 
| `-` | Horizontal-line marker | 