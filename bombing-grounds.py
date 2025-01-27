import matplotlib.pyplot as pp

overs = [1, 2, 3, 4]
runs = [6, 18, 10, 5]

pp.bar(overs, runs, color="m")
pp.xlabel("Overs")
pp.ylabel("Runs")
pp.title("Bowling Spell Analysis")
pp.show()
