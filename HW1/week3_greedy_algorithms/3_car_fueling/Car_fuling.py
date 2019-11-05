fuel = m
for i in range(len(stations)):
    fuel = fuel - stations[i]
    if fuel > stations[i+1]:
        continue
    else:
        charge it