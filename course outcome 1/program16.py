#Create a single string separated with space from two strings by swapping the 
#character at position 1
a=input("enter the 1st string:")
b=input("enter the 2nd string:")
a1=a[0]
a2=a[1:]
b1=b[0]
b2=b[1:]
print(b1+a2+" "+a1+b2)
