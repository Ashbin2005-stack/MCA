import math
def area(l,b):
    return l*b
def perimeter(l,b):
    return 2*l+b
l=int(input("Enter the length of the rectangle"))
b=int(input("Enter the length of the rectangle"))

print("The area of the rectangle is ",area(l,b))
print("The perimeter of the rectangle is ",perimeter(l,b))