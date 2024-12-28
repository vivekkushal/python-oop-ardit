# class Person:

#     def __init__(self, n, a):
#         self.name = n
#         self.age = a


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if (self.x > rectangle.lower_left.x and self.x < rectangle.upper_right.x) \
            and (self.y > rectangle.lower_left.y and self.y < rectangle.upper_right.y):
            return True
        return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 +
                (self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        length = abs(self.point2.x - self.point1.x)
        breadth = abs(self.point2.y - self.point1.y)
        return length * breadth



# point1 = Point(3, 4)
# point_origin = Point(0, 0)

# print(point1.distance_from_point(point_origin))

# pointx = Point(6, 7)
# rectanglex = Rectangle(Point(5, 6), Point(7, 9))
# print(pointx.falls_in_rectangle(rectanglex))

from random import randint

rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
print("Rectangle coordinates:", rectangle.lower_left.x, rectangle.lower_left.y, \
    "and", rectangle.upper_right.x, rectangle.upper_right.y)

x = int(input("Guess 'x' coordinate: "))
y = int(input("Guess 'y' coordinate: "))
point = Point(x, y)
print("Your point was inside the rectangle:", point.falls_in_rectangle(rectangle))
