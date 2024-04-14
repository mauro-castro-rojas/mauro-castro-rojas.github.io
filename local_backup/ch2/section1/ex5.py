import numpy as np
import matplotlib.pyplot as plt

# Given equation: y = 40t - 16t^2

# Time values for analysis
time_values = np.array([2.5, 2.1, 2.05, 2.01, 2.001])

# Function to calculate height at a given time
def height_eq(t):
    return (40 * t) - (16 * t**2)

initial_time = 2.0

average_velocities = []
for time in time_values:
    change_in_time = time - initial_time
    change_in_height = height_eq(time) - height_eq(initial_time)
    average_velocity = abs(change_in_height / change_in_time)
    average_velocities.append(average_velocity)
    print(f"Average velocity: {average_velocity} , for time period: {change_in_time}")



# Plot the height function
t_values = np.linspace(0, 3, 100)
y_values = height_eq(t_values)

plt.plot(t_values, y_values)
plt.title("Height vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Height (ft)")
plt.grid(True)
plt.show()
