import math

print("Weather Model Input (ax² + bx + c = 0)")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Weather event changes at: {x1:.2f} and {x2:.2f}")
else:
    print("No real weather pattern shift.")
