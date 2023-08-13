
# MATRIC NO: 20/30GD054
# DEPARTMENT: MECHANICAL ENGINEERING
# COURSE: ELE276 ASSIGNMENT

# ALGORITHM FOR THE SOLUTION OF THE QUADRATIC EQUATION USING THE FORMULAR METHOD

# Input the coefficients of the quadratic equation: a, b, and c.
# Calculate the discriminant D using the formula: D = b^2 - 4ac.
# If D is negative, display "No real roots" and stop.
# If D is non-negative:
# a. Calculate two solutions x1 and x2 using the formulas:
# x1 = (-b + √D) / (2a)
# x2 = (-b - √D) / (2a)
# b. Display the solutions x1 and x2.
# This algorithm outlines the steps to calculate the solutions of a quadratic equation using the quadratic formula.


# Main prograM


import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Check for real roots
    if D < 0:
        return None  # No real roots
    
    # Calculate the solutions
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    
    return x1, x2

# Input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
solutions = solve_quadratic(a, b, c)

if solutions is None:
    print("No real roots")
else:
    x1, x2 = solutions
    print("Solutions: x1 =", x1, "x2 =", x2)


