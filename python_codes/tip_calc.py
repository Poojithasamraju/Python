print("Welcome to the tip calculater")
bill=input("What was the total bill? $")
per=input("What percentge tip would you like to give? 10,12 or 15: ")
split=input("How many people to split the bill? ")
b=float(bill)
p=int(per)/100
s=int(split)
tip=(b*p)
total=tip+b
pay=total/s
print("Each person should pay: $")
print(float(round(pay,2)))

