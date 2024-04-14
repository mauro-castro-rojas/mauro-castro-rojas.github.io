import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sympy as sp

def curve_function(x):
    return 1/(x**2)

x_vals = np.linspace(-10, 10, 200)
y_vals = curve_function(x_vals)


x = sp.symbols('x') # Define symbolic variable
f_prime = sp.diff(curve_function(x), x) # Compute the derivative symbolically
f_prime_func = sp.lambdify(x, f_prime, 'numpy') # Convert the symbolic expression to a Python function
prime_y_vals = f_prime_func(x_vals) # Compute the y-values for the derivative

# Mask values where the derivative goes to infinity
threshold = 15760 # Adjust this threshold as needed
prime_y_vals[prime_y_vals > threshold] = np.nan
prime_y_vals[prime_y_vals < -threshold] = np.nan

# Figure and plot set up
fig, ax = plt.subplots(layout='constrained')


major_locator = MultipleLocator(1)
minor_locator = MultipleLocator(0.5)

ax.xaxis.set_major_locator(major_locator)
ax.xaxis.set_minor_locator(minor_locator)

curve_plot = ax.plot(x_vals, y_vals, label=r"$f(x)=\frac{1}{x^{2}}$")
derivative_plot = ax.plot(x_vals, prime_y_vals, label=r"$f'(x)=-\frac{2}{x^{3}}$")


ax.set_xlim([-10, 10])
ax.set_ylim([-8, 8])
ax.set_aspect(1)

ax.grid(which='major', linewidth='0.2', color=(0.2, 0.2, 0.2))  
ax.grid(which='minor', linewidth='0.1', color=(0.4, 0.4, 0.4))  

#ax.axis('equal')
ax.set_xlabel('x label')  
ax.set_ylabel('y label') 
ax.legend()
ax.set_title("Curve")

plt.show()