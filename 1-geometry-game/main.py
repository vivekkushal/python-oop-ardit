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

    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right



point1 = Point(3, 4)
point_origin = Point(0, 0)

print(point1.distance_from_point(point_origin))

pointx = Point(6, 7)
rectanglex = Rectangle(Point(5, 6), Point(7, 9))
print(pointx.falls_in_rectangle(rectanglex))
