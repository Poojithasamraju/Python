h=float(input("enter the height in m= "))
w=float(input("enter the weight in kg= "))
bmi=round(w/h**2)
if bmi<18.5:
    print(f"your bmi is {bmi},underweight")
elif bmi<25:
    print(f"your bmi is {bmi},normal weight")
elif bmi<30:  
    print(f"your bmi is {bmi},overweight")
elif bmi<35:
    print(f"your bmi is {bmi},obese")
else:
    print(f"your bmi is {bmi},clinically obese")       