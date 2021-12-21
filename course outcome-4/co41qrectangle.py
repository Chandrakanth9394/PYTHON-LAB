class rectangle:
    def __init__(self):
        self.length=int(input("enter the length of 1st the rectangle:"))
        self.breadth=int(input("enter the breadth of the rectangle:"))


    def display(self):
        print("length",self.length)
        print("breadth",self.breadth)
        print("area",self.area())
        print("perimeter",self.perimeter())
        


    def area(self):
        return self.length*self.breadth
        
    def perimeter(self):
        return 2*(self.length+self.breadth)
        
r1=rectangle()
r2=rectangle()
r1.display()
r2.display()

if(r1.area()>r2.area()):
    print("area of 1st rectangle is larger")
else:
    print("area of 2nd rectangle is larger")
    
