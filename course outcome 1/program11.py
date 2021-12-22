#Find biggest of 3 numbers entered.
a=int(input("1st number :"))
b=int(input("2nd number :"))
c=int(input("3rd number :"))
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)

       
    
