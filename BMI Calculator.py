weight= float(input("Enter your Weight in kilograms: "))
height= float(input("Enter your Height in centimeters: "))
height= height/100
bmi = weight / height ** 2
print(f"Your Body Mass Index is {bmi}")
if bmi>30:
    print("You are Obese")
if 25<bmi<29.9:
    print("You are Overweight")
if 18.5<bmi<24.9:
    print("You have a normal weight. Good work.")
if bmi<18.5:
    print("You are underweight")

