# leap year counter but now a date calculator
def date_formatting(string):
    string=string.split("-")
    day,month,year=string
    day=int(day)
    month=int(month)
    year=int(year)
    return day,month,year

def date_validation(day,month,year,leap_status):
    month_days_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    leap_month_list=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    if leap_status is not True:
        if month > 12 or month < 1:
            return False
        elif  day >month_days_list[month] or day < 1:
            return False
        elif year < 0:
            return False
    else:
        if month > 12 or month < 1:
                return False
        elif  day >leap_month_list[month] or day < 1:
            return False
        elif year < 0:
            return False

def leap(year):
    if year % 4==0:
        if year % 100==0 and year % 400==0:
            return True
        elif year % 100 != 0:
            return True
        else:
            return False
    else:
        return False
    
def year_count(start):
    index=0
    counter=0
    while index < start:
        if leap(index)== True:
            counter += 1
        index += 1
    return counter

def total_year_count(year,counter):
    total=(365*((year-1)-counter))+(366*counter)
    return total
        
def days_of_same_year(start_day, start_month, end_day, end_month, leap_status):
    month_days_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    leap_month_list=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    if leap_status!= True:
           latter_sum=(sum(month_days_list[1:end_month])+end_day)
           former_sum=(sum(month_days_list[1:start_month])+start_day)
    else:
        latter_sum=(sum(leap_month_list[1:end_month])+end_day)
        former_sum=(sum(leap_month_list[1:start_month])+start_day)
    days= latter_sum-former_sum
    return days

def day_of_the_week(days_elapsed):
    days=["Friday","Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return (days[days_elapsed % 7])

if __name__=="__main__":
    while True:
        user_starting_date=date_formatting(input("Enter the starting date in this format dd-mm-yyyy: "))
        user_starting_day,user_starting_month,user_starting_year= user_starting_date
        leap_start_year_status=leap(user_starting_year)
        if date_validation( user_starting_day,user_starting_month,user_starting_year,leap_start_year_status) == False:
            print("Invalid date entered, please enter a valid date")
            continue
        user_ending_date=date_formatting(input("Enter the ending date in this format dd-mm-yyyy: "))
        user_ending_day,user_ending_month,user_ending_year=user_ending_date        
        leap_end_year_status=leap(user_ending_year)
        if date_validation( user_ending_day,user_ending_month,user_ending_year,leap_end_year_status) == False:
            print("Invalid date entered, please enter a valid date")
            continue
        starting_leap_count=year_count(user_starting_year)
        starting_year=((total_year_count(user_starting_year,starting_leap_count)))+(days_of_same_year(1,1,user_starting_day,user_starting_month,leap_start_year_status))
        ending_leap_count=year_count(user_ending_year)
        ending_year=((total_year_count(user_ending_year,ending_leap_count)))+(days_of_same_year(1,1,user_ending_day,user_ending_month,leap_end_year_status))
        elapsed_days=ending_year-starting_year
        print(f"The total number of days excluding the ending date are {elapsed_days} days")
        print(f"The total number of days including it are {elapsed_days+1} and the end day is a {day_of_the_week(elapsed_days+1)}.")
        program_status=input("Enter y to continue or n to exit: ").lower()
        if program_status=="n":
            break





