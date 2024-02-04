class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# Test the classes
if __name__ == "__main__":
    shape = Shape()
    print("Area of shape:", shape.area())

    square = Square(5)
    print("Area of square:", square.area())

