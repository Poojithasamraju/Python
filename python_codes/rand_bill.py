import random
random_bill=input("Give the names to choose for paying: ")
bill=random_bill.split(", ")
names=len(bill)
pay=random.randint(0,names-1)
payer=bill[pay]
print(f"the person to pay: {payer}")