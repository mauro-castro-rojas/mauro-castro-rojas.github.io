import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd

# The point P(2, -1) lies on the curve defined by the function f(x),
# if Q is the point (x, f(x)) find the slope of the secant line PQ 
# (correct to six decimal places)
# for each of the values in the x_values array

def function(x):
    return 1 / (1 - x)

def slope(y2, y1, x2, x1):
    return (y2 - y1) / (x2 - x1)

x_values = [1.5, 1.9, 1.99, 1.999, 2.001, 2.01, 2.1, 2.5]

# Calculate the slope of the secant line PQ for each x value
slopes = []
for x1 in x_values:
    y2 = -1
    x2 = 2
    y1 = function(x1)
    slope_calc = slope(y2, y1, x2, x1)  # Fix the secant_slope function call
    slopes.append(slope_calc)

# Create a dictionary from the arrays
data = {
    'X values': x_values,
    'Slopes': slopes,
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
# Display the DataFrame
print(df.to_string(index=False))


# Set a vector of data to plot the function
x_vals = np.linspace(-6, 6, 200)
# Evaluate the function with the vector
y_vals = function(x_vals)

#The tangent line is obtained by using the point-slope equation for a line
# The value m of the tangent is assumed to be 1 , given the data obtained
# when estimating the slopes of the secant lines. 

tangent_line = x_vals - 3

# Mask values where the derivative goes to infinity
threshold = 8 # Adjust this threshold as needed
y_vals[y_vals > threshold] = np.nan
y_vals[y_vals < -threshold] = np.nan

fig, ax = plt.subplots(layout='constrained')
ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_aspect(1)

major_locator = MultipleLocator(2)
minor_locator = MultipleLocator(0.5)
ax.xaxis.set_major_locator(major_locator)
ax.xaxis.set_minor_locator(minor_locator)
ax.yaxis.set_major_locator(major_locator)
ax.yaxis.set_minor_locator(minor_locator)
ax.grid(which='major', linewidth='0.1', color=(0.2, 0.2, 0.2))  
ax.grid(which='minor', linewidth='0.05', color=(0.4, 0.4, 0.4))  

ax.plot(x_vals, y_vals, label=r"$f(x)=\frac{1}{1- x}$")
ax.plot(x_vals, tangent_line, label="Tangent line at point (2,-1)")
ax.plot(df['X values'], df['Slopes'], marker='o', linestyle='-', color='b')

# Mark the point P(2, -1) on the plot
ax.scatter(2, -1, color='red', label="Point P(2, -1)")

ax.set_xlabel('x label')  
ax.set_ylabel('y label') 
ax.legend()
ax.set_title("Curve")

plt.show()

