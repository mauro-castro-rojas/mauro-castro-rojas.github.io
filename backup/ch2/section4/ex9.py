# 9. The point P(1, 0) lies on the curve y = sin(10*pi/x).
# (a) If Q is the point (x, sin(10*pi/x)), find the slope of the
# secant line PQ (correct to four decimal places) for
# x = 2, 1.5, 1.4, 1.3, 1.2, 1.1, 0.5, 0.6, 0.7, 0.8, 0.9.
# Do the slopes appear to be approaching a limit?

import numpy as np

# Function to calculate the slope of the secant line
def calculate_secant_slope(x):
    y_Q = np.sin(10 * np.pi / x)
    slope = (y_Q - 0) / (x - 1)
    return slope

# Given x values
x_values = [2, 1.5, 1.4, 1.3, 1.2, 1.1, 0.5, 0.6, 0.7, 0.8, 0.9]

# Calculate and print the slopes
for x in x_values:
    slope = calculate_secant_slope(x)
    print(f"Slope for x = {x:.4f}: {slope:.4f}")

# Calculate the limit as x approaches 0
limit_as_x_approaches_0 = calculate_secant_slope(0.001)
print(f"Limit as x approaches 0: {limit_as_x_approaches_0:.4f}")
