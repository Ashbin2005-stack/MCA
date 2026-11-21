class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def __lt__(self, other):
        return self.area() < other.area()


# Creating two rectangle objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

# Comparing the areas
if r1 < r2:
    print("Area of Rectangle 1 is smaller")
else:
    print("Area of Rectangle 1 is greater or equal")


print("Area of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())
