#generate positive list of numbers from a given list of intergers
a=[-4,-3,-2,-1,1,2,3,4,-5,-6,-7,-8,-9]
b=[x for x in a if x>0]
print(b)

#b.Square of N numbers
a=int(input("enter the limit:"))
print([x*x for x in range(a+1)])


#c.Form a list of vowels selected from a given word
word=input("enter the word=")
vowel=["A","E","I","O","U","a","e","i","o","u"]
list=[x for x in word if x in vowel]
print(list)


#d.List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
word=input("enter the word=")
list0=[ord(x) for x in word]
print(list0)
