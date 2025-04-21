from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def print_all_info(self):
        print(f"Area: {self.get_area()}, Perimeter: {self.get_perimeter()}")

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    

class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = width

class Triangle(Shape):
    def __init__(self, a, b, c):
        s = (a + b + c) / 2
        self.area = math.sqrt(s * ((s-a)*(s-b)*(s-c)))
        self.perimeter = a + b + c

    def get_area(self):
        return self.area
    
    def get_perimeter(self):
        return self.perimeter
