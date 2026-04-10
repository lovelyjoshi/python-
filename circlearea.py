import math

def area_of_circle(radius):
    area = math.pi * radius * radius
    return area

# Example
r = float(input("Enter radius: "))
print("Area of circle =", area_of_circle(r))