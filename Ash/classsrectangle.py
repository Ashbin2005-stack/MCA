class Rectangle:
    def __init__ (self,l,b):
      self.l=l
      self.b=b
#constructor
    def area(self):
        return self.l*self.b

    def perimeter(self):
        return 2*self.l*self.b
#object
r1=Rectangle(10,5)
r2=Rectangle(8,6)
#printing value
print("Rectangle 1")
print("Length:",r1.l)
print("Length:",r1.b)
print("Area:",r1.area())
print("Perimeter:",r1.perimeter())

print("Rectangle 2")
print("Length:",r2.l)
print("Length:",r2.b)
print("Area:",r2.area())
print("Perimeter:",r2.perimeter())

#Compairing

if(r1.area()>r2.area()):
    print("Rectangle 1 has greater area")
elif(r1.area()<r2.area()):
     print("Rectangle 2 has greater area")
else:
    print("both have same area")