# The displacement (in centimeters) of a particle moving
# back and forth along a straight line is given by the equation
# of motion s = 2sin pi*t + 3cos pi*t, where t is measured in
# seconds.
# (a) Find the average velocity during each time period:
# (i) [1, 2] (ii) [1, 1.1]
# (iii) [1, 1.01] (iv) [1, 1.001]

import numpy as np
import math

# Function to calculate displacement at a given time
def displacement_equation(t):
    return 2 * np.sin(math.pi * t) + 3 * np.cos(math.pi * t)

# Given time intervals
time_intervals = [[1, 2], [1, 1.1], [1, 1.01], [1, 1.001], [1,1.00001]]

# Function to calculate average velocity
def calculate_average_velocity(initial_time, final_time):
    initial_displacement = displacement_equation(initial_time)
    final_displacement = displacement_equation(final_time)
    change_in_displacement = final_displacement - initial_displacement
    change_in_time = final_time - initial_time
    average_velocity = change_in_displacement / change_in_time
    return average_velocity

# Calculate and print average velocities for each time interval
for interval in time_intervals:
    initial_time, final_time = interval
    average_velocity = abs(calculate_average_velocity(initial_time, final_time))
    print(f"Average velocity for time interval {interval}: {average_velocity:.4f} cm/s")
