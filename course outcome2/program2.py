#Generate Fibonacci series of N terms
limit=int(input("enter the limit:"))
a=0
b=1
print(a)
print(b)
for i in range (1,limit):
    sum=a+b
    print(sum)
    a=b
    b=sum
    
    
