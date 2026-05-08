# day calculator
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
    
def leap_year_count(start,end):
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

def days_of_different_years(start_year,start_month,start_day,end_year,end_month,end_day,start_leap_status,end_leap_status):
    month_days_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    leap_month_list=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    if start_leap_status!= True:
        starting_sum=(sum(month_days_list[start_month:12]))-(month_days_list[start_month]-start_day)
    else:
        starting_sum=(sum(leap_month_list[start_month:12]))-(month_days_list[start_month]-start_day)
    print(starting_sum)
    if end_leap_status != True:
        ending_sum=(sum(month_days_list[1:end_month-1]))+end_day
    else:
        ending_sum=(sum(leap_month_list[1:end_month-1]))+end_day
    print(ending_sum)
    days= starting_sum+ending_sum
    return days  
    
if __name__=="__main__":
    days=days_of_different_years(2025,12,25,2026,1,15,False,False)
    print(days)


def total_days_count(start_year,start_month,start_day,end_year,end_month,end_day,start_leap_status,end_leap_status,counter):
    if start_year==end_year:
        return days_of_same_year(start_day,start_month,end_day,end_month,start_leap_status)    
    else:


if __name__=="__main__":
    while True:
        user_starting_year=int(input("Enter the year: "))
        leap_start_year_status=leap(user_starting_year)
        user_starting_month=int(input("Starting Month: "))
        user_starting_day=int(input("Starting Day: "))
        user_ending_month=int(input("Ending Month: "))
        user_ending_day=int(input("Ending Day: "))
        user_ending_year=int(input("Enter the ending year: "))
        leap_end_year_status=leap(user_ending_year)

    
