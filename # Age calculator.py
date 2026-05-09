# Age calculator
year=int(input("What year were you born in? "))
month=int(input("What month were you born in (1-12) "))
age_m= (year*12)+ month
cyear=int(input("What is the current year? "))
cmonth=int(input("What is the current month "))
age_mc= (cyear*12)+ cmonth

current_age1=(age_mc-age_m)/12
current_age2=(age_mc-age_m)//12
print(f"You are {current_age2} years,{int((current_age1-current_age2)*12)} months old") # I multiplied the months here by 10 because I thought that all I needed to do was
# get the decimal out, but the fraction itself is from 12 months- a year- so yeah- 1 mistake. But overall wasn't so bad.

if current_age1 <= 10:
    print("You are a child! Enjoy your childhood!")

elif 18>current_age1>10:
    print("You are a Teenager. Enjoy your Adolesence!")

elif 30>current_age1>18:
    print("You are a young Adult.")

elif 50>current_age1>30:
    print("You are an Adult.")

elif 60>current_age1>50:
    print("You are Middle Aged.")

else:
    print("You are old.")
