import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

# Test the Point class
if __name__ == "__main__":
    # Create two points
    point1 = Point(2, 3)
    point2 = Point(5, 7)

    # Display the coordinates of point1
    point1.show()

    # Move point2 to new coordinates
    point2.move(10, 15)
    point2.show()

    # Compute the distance between point1 and point2
    distance = point1.dist(point2)
    print("Distance between the two points:", distance)
