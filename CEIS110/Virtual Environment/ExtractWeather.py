#Purpose: Create a plot comparing humidity to temperature.
#Name: Harrison Olvera
#Date: 10/8/23
import pandas as pd
import matplotlib.pyplot as plt

# Read the weather data into a Pandas DataFrame.
df2 = pd.read_csv('formatdata2.csv')

# Create a Matplotlib figure.
fig, ax = plt.subplots()

# Plot the weather data using the Matplotlib `plot()` function.
ax.plot(df2['Fahrenheit'], df2['Humidity'])

# Add labels and titles to the plot.
ax.set_xlabel('Temperature')
ax.set_ylabel('Humidity')
ax.set_title('Weather Data')

# Show the plot.
plt.show()
