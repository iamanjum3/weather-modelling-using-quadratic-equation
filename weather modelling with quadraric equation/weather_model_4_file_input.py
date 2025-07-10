import math

with open("weather_input.txt", "r") as file:
    for line in file:
        a, b, c = map(float, line.split())
        print(f"\nEquation: {a}x² + {b}x + {c} = 0")
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Weather turning points: {x1:.2f}, {x2:.2f}")
        else:
            print("No real turning points in this weather model.")
