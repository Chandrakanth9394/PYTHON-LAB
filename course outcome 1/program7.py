#Enter 2 lists of integers.
#Check (a) Whether list are of same lengthCheck
#b)whether list sums 
#c)whether any value occur in both tosame value

l1=[2,3,4,5,6,7]
l2=[9,8,7,6,5,4,3]
print(l1)
print(l2)
if len(l1)==len(l2):
    print("the length are same")
else:
    print("the length are not same")

if sum(l1)==sum(l2):
    print("the sum are same")
else:
    print("the sum are not same")

l3=[x for x in l1 if x in l2 ]
if len(l3)<1:
    print("no value please enter the values")
else:
    print("the common values are:",l3)
    

    
    
    
        
   
