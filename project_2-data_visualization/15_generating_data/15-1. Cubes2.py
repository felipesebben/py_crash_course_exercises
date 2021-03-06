import matplotlib.pyplot as plt

x_values = range(5001)
cubes = [x**3 for x in x_values]

# Set plot
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, s=10)

# Set chart title and label axes.
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the range for each axis.
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

# Show plot.
plt.show()
