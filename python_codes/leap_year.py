year=int(input("enter the year:"))
if year%4==0:
    print("the year is leap")
elif year%100==0:
    print("the year is not leap")
elif year%400==0:
    print("the year is leap")
else:
    print("the year is not leap")
