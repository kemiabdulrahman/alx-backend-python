
# DEPARTMENT: MECHANICAL ENGINEERING
# COURSE: ELE276 ASSIGNMENT



# Algorithm for Cylindrical tube question:

# Input the values of the cylinder's height 'h' and base radius 'r'.
# Calculate the volume 'V' of the cylinder using the formula: V = π * r^2 * h.
# Calculate the curved surface area 'CSA' using the formula: CSA = 2 * π * r * h.
# Calculate the total surface area 'TSA' using the formula: TSA = 2 * π * r * (r + h).
# Display the calculated values of volume, curved surface area, and total surface area.


import math

def calculate_cylinder_properties(h, r):
    # Calculate volume
    V = math.pi * r**2 * h
    
    # Calculate curved surface area
    CSA = 2 * math.pi * r * h
    
    # Calculate total surface area
    TSA = 2 * math.pi * r * (r + h)
    
    return V, CSA, TSA

# Input values
h = float(input("Enter height of the cylinder (m): "))
r = float(input("Enter base radius of the cylinder (m): "))

# Calculate cylinder properties
V, CSA, TSA = calculate_cylinder_properties(h, r)

# Display results
print("Volume of the cylinder V =", V, "cubic meters")
print("Curved Surface Area CSA =", CSA, "square meters")
print("Total Surface Area TSA =", TSA, "square meters")
