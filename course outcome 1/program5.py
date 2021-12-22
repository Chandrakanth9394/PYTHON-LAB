#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead
a=[]
a=[int(item) for item in input("Enter the list items : ").split()]
print("INPUT IS", a)
x=["over" if x>100 else x for x in a]
a=list(x)
print(a)
