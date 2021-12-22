#Store a list of first names. Count the occurrences of ‘a’ within the list
name=["akon","bkon","ckon","dkon"]
n=0
for x in name:
    n=n+x.count("o")
print("number of 'o'=",n)
