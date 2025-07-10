# Weather modeling: fixed values for temperature prediction
a = 1
b = -6
c = 8

import math

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Predicted change points: {x1:.2f}, {x2:.2f}")
else:
    print("No real change points in weather model.")
