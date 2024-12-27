# class Person:
    
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lower_left, upper_right):
        if (self.x > lower_left[0] and self.x < upper_right[0]) \
            and (self.y > lower_left[1] and self.y < upper_right[1]):
            return True
        return False
    
    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5


point1 = Point(3, 4)
point2 = Point(6, 7)

point3 = Point(4, 5)

print(point3.falls_in_rectangle((3, 4),(6, 7)))
print(point1.distance(0, 0))
