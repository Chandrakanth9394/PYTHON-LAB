#Display future leap years from current year to a final year entered by user.
x=int(input("Enter a future year :"))
y=int(input("Enter the current year:"))

while (y<=x):
    if y%100==0:
        if y%400==0:
            print(y)
    elif y%4==0:
        print(y)
    y+=1
