# b
# Use a calculator to estimate the values of the limits:
# As h approaches 0 of (2.7^h - 1)/h
# As h approaches 0 of (2.8^h - 1)/h

#correct to two decimal places. What can you conclude about the value of e ?

from sympy import symbols, limit

# Define the variable and the expression
h = symbols('h')
expression1 = (2.7**h - 1) / h
expression2 = (2.8**h - 1) / h

# Calculate the limit as x approaches 1
limit_result1 = limit(expression1, h, 0)
limit_result2 = limit(expression2, h, 0)

print(f"The limit as h approaches 0 of (2.7^h - 1)/h is: {limit_result1.evalf(2)}")
print(f"The limit as h approaches 0 of (2.8^h - 1)/h is: {limit_result2.evalf(2)}")