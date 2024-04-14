import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def curve_function(x):
    return x**(3/2)

# Plot the curve
x_vals = np.linspace(0, 3, 100)
y_vals = curve_function(x_vals)

# Plot the tangent lineand the normal line of the function
tangent_line = ((3/2) * x_vals) - (1/2)
normal_line = ((-2/3)* x_vals) + (5/3)


# Plot settings
# Define the width and height of the figure in inches
width = 7
height = 7

fig, ax = plt.subplots(figsize=(width, height), layout='constrained')

#plot the curve , normal and tangent lines
ax.plot(x_vals, y_vals, label="Curve y = 1 / (1 - x)")
ax.plot(x_vals, tangent_line, label="Tangent Line")
ax.plot(x_vals, normal_line, label="Normal Line")

# Mark the point P(1, 1) on the plot
ax.scatter(1, 1, color='red', label="Point P(1, 1)")

# set plot config
ax.axis('equal') # set a 1:1 scale in XY axis (square grid)
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.legend()

# Enable the grid
ax.grid(True)

# Define the step size for the ticks
step = 1

# Calculate the tick locations using numpy.arange
x_ticks = np.arange(-1, 3, step)
y_ticks = np.arange(0, 5, step)


# Set the tick locations on the x and y axes
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.set_yticks(np.arange(0, 5, 0.2), minor=True)



ax.set_title("Curve, Tangent, and normal Lines")
plt.show()