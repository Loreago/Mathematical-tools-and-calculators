# BMI Calculator v2
def units(system):
    if system== "imperial":
        height_feet=int(input("Enter your height in feet. (E.g. if 5 ft 10, enter 5:) "))*12
        height_inches=float(input("Enter the inches part of your height (E.g. if 5 ft 10, enter 10)"))+height_feet
        weight_pounds=float(input("Enter your weight in lbs: "))
        return (height_inches, weight_pounds, 703, "lbs", "imperial")
    
    elif system== "metric":
        height_metric=float(input("Enter your height in centimeters: "))/100
        weight_metric=float(input("Enter your weight in kilograms: "))
        return (height_metric, weight_metric, 1, "kgs", "metric")
        

def bmi(height, weight, conversion_factor):
    bmi= (weight/(height**2))*conversion_factor
    return bmi

def bmi_classification(bmi):
    if bmi <16:
        classification= "Severe Thinness"
        return classification
    elif 16<= bmi < 17:
        classification= "Moderate Thinness"
        return classification
    elif 17<= bmi < 18.5:
        classification= "Mild Thinness"
        return classification
    elif 18.5<= bmi < 25:
        classification= "Normal"
        return classification
    elif 25<= bmi < 30:
        classification= "Overweight"
        return classification
    elif 30<= bmi < 35:
        classification= "Obese Class I"
        return classification
    elif 35<= bmi < 40:
        classification= "Obese Class II"
        return classification
    elif bmi>=40:
        classification= "Obese Class III"
        return classification


def bmi_prime(bodymass):
    bmi_prime= bodymass/25
    return bmi_prime

def ponderal_index(height, weight, system):
    if system == "imperial":
        ponderal_i= height/(weight**(1/3))
        return ponderal_i
    elif system == "metric":
        ponderal_i=weight/(height**3)
        return ponderal_i
    

def ideal_range(height, conversion_factor):
    lower_limit=18.5*(height**2)/conversion_factor
    upper_limit=25*(height**2)/conversion_factor
    return lower_limit, upper_limit






if __name__== "__main__":
    user_units= units(input("Enter your unit system. 'Metric' or 'Imperial': ").lower()) 
    user_height, user_weight, conversion_factor, weight_unit, system = user_units 
    user_bmi=bmi(user_height, user_weight, conversion_factor)
    print()
    print(f"You have a BMI of {user_bmi:.1f}")
    print(f"You have a BMI Prime value of {bmi_prime(user_bmi):.1f}")
    print(f"Your BMI is classified as {bmi_classification(user_bmi)}")
    print(f"Your Ponderal index is {ponderal_index(user_height, user_weight, system):.1f} in {system} units.")
    lower_limit, upper_limit=ideal_range(user_height, conversion_factor)
    if 18.5<= user_bmi < 25:
        print("Congratulations! Your BMI is in the ideal range.")
    else:
        print("A healthy BMI would be in the range of 18.5 to 25")
        print(f"Your ideal weight range would be {lower_limit:.1f} {weight_unit} to {upper_limit:.1f} {weight_unit}")
        if user_weight < lower_limit: 
            print(f"Gain {(lower_limit-user_weight):.1f} {weight_unit} to reach a weight of {lower_limit:.1f} {weight_unit}")
        else:
            print(f"Lose {(user_weight-upper_limit):.1f} {weight_unit} to reach a weight of {upper_limit:.1f} {weight_unit}")

