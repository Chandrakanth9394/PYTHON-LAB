#Print out all colors from color-list1 not contained in color-list2
color1=["red","violet","yellow","black","blue"]
color2=["green","violet","yellow","orange","black"]
s1=set(color1)
s2=set(color2)
s3=s1.difference(s2)
print(list(s3))
