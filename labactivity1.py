def Polygon(name):
    if name == "Triangle" or name == "triangle" or name == "TRIANGLE":
        return 3
    elif name == "Square" or name == "square" or name == "SQUARE":
        return 4
    elif name == "Rectangle" or name == "rectangle" or name == "RECTANGLE":
        return 4
    else:
        return None

name = input("Name of polygon: ")

try:
    name = str(name)
    if name not in ["Triangle", "triangle", "TRIANGLE", "Square", "square", "SQUARE", "Rectangle","rectangle", "RECTANGLE" ]:
        print("Polygon name not included.")
    else:
        side = Polygon(name)
        print(name + " is a polygon which has " + str(side) + " sides.")
except:
    print("Invalid input. Please enter a valid polygon name.")
class Triangle:
    def calculate_area(self):
        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))
        c = float(input('Enter third side: '))
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("The area of the triangle is:", area, "square units.")


class Rectangle:
    def calculate_area(self):
        length = float(input('Enter the length: '))
        width = float(input('Enter the width: '))
        area = length * width
        print("The area of the rectangle is:", area, "square units.")

class Square:
    def calculate_area(self):
        side = float(input('Enter the side length: '))
        area = side * side
        print("Area of the square is: ", area, "square units.")

def main():
    polygon_type = input("Enter the polygon type (Triangle, Rectangle, Square): ").strip().lower()

    if polygon_type == "triangle":
        triangle = Triangle()
        triangle.calculate_area()
    elif polygon_type == "rectangle":
        rectangle = Rectangle()
        rectangle.calculate_area()
    elif polygon_type == "square":
        square = Square()
        square.calculate_area()
    else:
        print("Invalid polygon type.")

if __name__ == "__main__":
    main()