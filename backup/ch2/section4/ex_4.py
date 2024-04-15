import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


pi_value = np.pi


def cosine_function(x):
    return np.cos(pi_value*x)


print(cosine_function(0))
# Define the slope of the secant line between two points (x1, y1) and (x2, y2)
def secant_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)

# Values of x for which we need to calculate the secant slope
x_values = [0, 0.4, 0.49, 0.499, 0.501, 0.51, 0.6, 1]

# Calculate the slope of the secant line PQ for each x value
slopes = []
y_values = []
for x in x_values:
    y1 = cosine_function(x)
    y2 = cosine_function(0.5)
    slope = secant_slope(x, 0.5, y1, y2)  # Fix the secant_slope function call
    slopes.append(slope)
    y_values.append(y1)
# Create a dictionary from the arrays
data = {
    'X values': x_values,
    'Y values': y_values,
    'Slopes': slopes
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# Estimate the slope of the tangent line at point P(2, -1)
tangent_slope = np.mean(slopes)

# Equation of the tangent line: y = mx + b, where m is the slope and b is the y-intercept
# At point P(2, -1), the tangent line is: y = tangent_slope * (x - 2) - 1

# Plot the curve
x_vals = np.linspace(-5, 5, 100)
y_vals = cosine_function(x_vals)

plt.plot(x_vals, y_vals, label="Curve y = 1 / (1 - x)")

# Plot the tangent line at point P(2, -1)
tangent_line = tangent_slope * (x_vals - 0.5)
plt.plot(x_vals, tangent_line, label="Tangent Line at P(2, -1)")

# Mark the point P(2, -1) on the plot
plt.scatter(0.5, 0, color='red', label="Point P(0.5, 0)")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.title("Curve and Tangent Line")
plt.show()

# Print the estimated slope of the tangent line
print(f"Estimated slope of the tangent line at P(2, -1): {tangent_slope:.6f}")
