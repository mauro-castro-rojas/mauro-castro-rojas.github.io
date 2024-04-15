import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

sy.init_printing(use_unicode=True)

x = sy.symbols("x")

f = (-2) * sy.exp(x)
print(f)
dx = sy.diff(f,x)
#dx = dx.doit()

print(dx)

#convert to a numerical function for plotting

lmbdfy = sy.lambdify(x, dx)

x_vals = np.linspace(-3,10,200)
y_vals = lmbdfy(x_vals)

plt.plot(x_vals,y_vals)
plt.show()