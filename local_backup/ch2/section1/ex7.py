# The table shows the position of a motorcyclist after accelerating
# from rest.
# t seconds: 0 1   2    3    4    5     6
# s (feet):  0 4.9 20.6 46.5 79.2 124.8 176.7
# (a) Find the average velocity for each time period:
# (i) (2, 4) (ii) (3, 4) (iii) (4, 5) (iv) (4, 6)
import matplotlib.pyplot as plt

# Given positions (s) and times (t)
positions = [0, 4.9, 20.6, 46.5, 79.2, 124.8, 176.7]
times = [0, 1, 2, 3, 4, 5, 6]

# Create an array of time intervals
time_intervals = [[2, 4], [3, 4], [4, 5], [4, 6]]

# Function to calculate average velocity
def calculate_average_velocity(y1, y2, x1, x2):
    return (y2 - y1) / (x2 - x1)

# Calculate and print average velocities for each time interval
for interval in time_intervals:
    x1, x2 = interval
    y1 = positions[x1]
    y2 = positions[x2]
    
    average_velocity = calculate_average_velocity(y1, y2, x1, x2)
    
    print(f"Average velocity for time interval {interval}: {average_velocity} ft/s")


# Plot the points
plt.plot(times, positions, marker='o', linestyle='-', color='b')
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (ft)")
plt.grid(True)
plt.show()




# Indices for estimating slopes
slope_indices = [[0, 1], [0, 2], [0, 3], [3, 4], [3, 5], [3, 6]]

# Array to store slopes
slopes = []

# Calculate and store slopes
for indices in slope_indices:
    x1, x2 = indices
    y1 = positions[x1]
    y2 = positions[x2]
    
    average_velocity = calculate_average_velocity(y1, y2, x1, x2)
    
    print(f"Average velocity for time interval {indices}: {average_velocity} ft/s")