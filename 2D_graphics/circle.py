import math
def area(r):
    return math.pi*r*r
def perimeter(r):
    return 2*math.pi*r

r= float(input("Enter the radius of the circle: "))
print("The area of the circle is ",area(r))
print("Perimeter of the circle is ",perimeter(r))