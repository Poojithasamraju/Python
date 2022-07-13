import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['#', '$', '&', '*', '!', '^', '?']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
let=int(input("how many letters do you want?"))
sym=int(input("how many symbols do you want?"))
num=int(input("how many numbers do you want?"))
password=[]
for char in range(1,let+1):
 password.append(random.choice(letters))
for char in range(1,sym+1):
 password+=random.choice(symbols)
for char in range(1,num+1):
 password+=random.choice(numbers)
 random.shuffle(password)
final="" 
for char in password:
    final+=char
print(final)







