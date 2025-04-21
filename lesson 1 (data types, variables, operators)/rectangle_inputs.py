"""
Problem: Make two variables, the width and height of a rectangle. Based on those, print the perimeter and area of the rectangle.
"""

width = int(input("Input the width of the rectangle: "))
height = int(input("Input the height of the rectangle: "))

print(2 * (width + height))     # perimeter
print(width * height)           # area