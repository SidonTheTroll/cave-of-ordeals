# Part 2: Data Visualization 
## 16. Plot following data on a line chart and follow the given instructions. 

| Day | Monday | Tuesday | Wednesday | Thursday | Friday | 
|-|-|-|-|-|-|
| Income | 510 | 350 | 470 | 580 | 600 | 

1. Write a title for the chart "The Weekly Income Report".
2. Write the appropriate titles of both the axes. 
3. Write code to display legends.
4. Display red color for the line.
5. Use the line style: dashed
6. Display diamond style markers on data points.

```python
import matplotlib.pyplot as plt

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
inc = [510, 350, 475, 580, 800]

plt.plot(day, inc, label="Income", color="r", linestyle="dashed", marker="D")
plt.title("The Weekly Income Report")

plt.xlabel("Days")
plt.ylabel("Income")
plt.legend()
plt.show()
```

## 17. Consider the following data of a medical store and plot the data on the line chart and customize the chart as you wish: 
| Month | Masks | Sanitizer | Hand Wash | 
|:-:|:-:|:-:|:-:|
| March | 1500 | 4400 | 6500 | 
| April | 3500 | 4500 | 5000 | 
| May | 6500 | 5500 | 5800 | 
| June | 6700 | 6000 | 6300 | 
| July | 6000 | 5600 | 6200 | 
| August | 6800 | 6300 | 4500 | 

```python
import matplotlib.pyplot as pp

mon = ["March", "April", "May", "June", "July", "August"]
mask = [1500, 3500, 6500, 6700, 6000, 6800]
san = [4400, 4500, 4400, 6000, 5600, 6300]
hw = [6500, 5000, 5800, 6300, 6200, 4500]

pp.plot(mon, mask, label="Mask", color="g", linestyle="dashed", linewidth=4, marker="o", markerfacecolor="k", markeredgecolor="r")
pp.plot(mon, san, label="Sanitezer", color="b", linestyle="dashed", linewidth=4, marker="3", markerfacecolor="k", markeredgecolor="g")
pp.plot(mon, hw, label="Handwash", color="r", linestyle="dashed", linewidth=4, marker="v", markerfacecolor="k", markeredgecolor="b")

pp.title("Fitwell Medical Store")
pp.xlabel("Months")
pp.ylabel("Covid Protections")
pp.legend()
pp.show()
```

## 18. Use above data and subplot sanitizer data and handwash data.
```python
import matplotlib.pyplot as pp

mon = ["March", "April", "May", "June", "July", "August"]
san = [4400, 4500, 4400, 6000, 5600, 6300]
hw = [6500, 5000, 5800, 6300, 6200, 4500]

# Subplot 1 for Sanitizer
pp.subplot(2, 1, 1)
pp.plot(mon, san, label="Sanitizer", color="b", linestyle="dashed", linewidth=4, marker="o", markerfacecolor="k", markeredgecolor="r")
pp.title("Fitwell Medical Store")
pp.legend()

# Subplot 2 for Handwash
pp.subplot(2, 1, 2)
pp.plot(mon, hw, label="Handwash", color="r", linestyle="dashed", linewidth=4, marker="v", markerfacecolor="k", markeredgecolor="b")
pp.xlabel("Months")
pp.ylabel("Covid Protections")
pp.legend()
pp.show()
```

## 19. Display following bowling figures through bar chart:
| Overs | Runs | 
|:-:|:-:|
| 1 | 6 | 
| 2 | 18 | 
| 3 | 10 | 
| 4 | 5 | 

```python
import matplotlib.pyplot as pp

overs = [1, 2, 3, 4]
runs = [6, 18, 10, 5]

pp.bar(overs, runs, color="m")
pp.xlabel("Overs")
pp.ylabel("Runs")
pp.title("Bowling Spell Analysis")
pp.show()
``` 
