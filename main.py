import math

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def cylinder_volume(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * radius ** 2 * height

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    return (4/3) * math.pi * radius ** 3

def grading_system(score):
    """Determine grade based on score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def sum_of_elements(numbers):
    """Return the sum of all elements in a list."""
    return sum(numbers)

# Example
print("Rectangle Area:", rectangle_area(5, 10))
print("Circle Area:", circle_area(7))
print("Cylinder Volume:", cylinder_volume(3, 5))
print("Sphere Volume:", sphere_volume(4))
print("Grade:", grading_system(85))
print("Sum of Elements:", sum_of_elements([1, 2, 3, 4, 5]))
