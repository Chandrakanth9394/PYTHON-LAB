class student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("roll no:",self.roll)
        print("name=",self.name)
        print("course name=",self.course)
class test(student):
    def __init__(self,roll,name,course,mark):
        student.__init__(self,roll,name,course)
        self.mark=mark
    def display_mark(self):
        self.display()
        print("marks=",self.mark)
s1=test(5,"Chandrakanth","MCA",500)
s1.display_mark()

                     
                
