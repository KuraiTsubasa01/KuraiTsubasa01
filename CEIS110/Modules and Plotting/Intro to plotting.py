#A program to plot ocean temperatures read from a file.
import matplotlib.pyplot as plt #The 'as' keyword renames an imported module or package

with open('ocean_temps.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

years = range(1850, 2012)

plt.plot(years, temps) #plots the data
plt.show() #displays the graph

#Plotting multiple lines in the same graph.
import matplotlib.pyplot as plt

with open('ocean_temp.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

temp_years = range(1850, 2012)
plt.plot(temp_years, temps)

pirate_years = range(1850, 2025, 25)
num_pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
plt.plot(pirate_years, num_pirates_thousands)
plt.show()