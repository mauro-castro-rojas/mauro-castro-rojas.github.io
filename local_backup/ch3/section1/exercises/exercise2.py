import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sympy as sy

def f(x):
    return sy.exp(x)

x = sy.symbols('x')  # Define symbolic variable

# Compute the derivative symbolically
dx = sy.diff(f(x), x)

# the lambdify function is used to convert symbolic expressions into 
# functions that can be evaluated with numerical values
f_func = sy.lambdify(x, f(x), 'numpy')
f_prime_func = sy.lambdify(x, dx, 'numpy')

x_vector = np.linspace(-3, 3, 200)
function_values = f_func(x_vector)
derivative_values = f_prime_func(x_vector)

# Figure and plot set up
fig, ax = plt.subplots(layout='constrained')

major_locator = MultipleLocator(2)
minor_locator = MultipleLocator(1)

ax.xaxis.set_major_locator(major_locator)
ax.xaxis.set_minor_locator(minor_locator)

curve_plot = ax.plot(x_vector, function_values, label='e^x', linestyle='-.', color='blue')
derivative_plot = ax.plot(x_vector, derivative_values, label="e^x (Derivative)", linestyle=':', color='red')

ax.set_xlim([-3, 3])
ax.set_ylim([-2, 30])
#ax.set_aspect(1)

ax.grid(which='major', linewidth='0.2', color=(0.2, 0.2, 0.2))
ax.grid(which='minor', linewidth='0.1', color=(0.4, 0.4, 0.4))

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.legend()
ax.set_title("Curve")

plt.show()
