from random import randint 
from fractions import Fraction

def likelihood_of_outcomes(number_of_outcomes: int,number_of_instances: int):
    outcome_dictionary={}
    number=1
    for items in range(0,number_of_outcomes):
        outcome_dictionary[number]=0
        if items==0:
            first_number=number
        elif items==number_of_outcomes-1:
            last_number=number
        number+=1
    for numbers in range(0,number_of_instances):
        outcome=randint(first_number,last_number)
        outcome_dictionary[outcome]+=1
    mathematical_probability=1/number_of_outcomes
    for items in outcome_dictionary:    
        empirical_likelihood=(outcome_dictionary[items])/number_of_instances
        outcome_dictionary[items]=mathematical_probability,empirical_likelihood,Fraction(mathematical_probability).limit_denominator(number_of_outcomes),Fraction(empirical_likelihood).limit_denominator(number_of_outcomes)
    return outcome_dictionary

if __name__=="__main__":    
    user_no_of_outcomes=int(input("Enter the number of possible outcomes: "))
    user_no_of_instances=int(input("Enter the number of instances you want to calculate the probability over: "))
    user_dictionary=(likelihood_of_outcomes(user_no_of_outcomes,user_no_of_instances))
    print(f"For an event with {user_no_of_outcomes} outcomes over {user_no_of_instances} instances: ")
    for items in user_dictionary:
        print(f"The mathematical probabilty of {items} occurring is {user_dictionary[items][0]:.3f} or {user_dictionary[items][2]}. Empirically for {user_no_of_instances} instances the probability is {user_dictionary[items][1]} or {user_dictionary[items][3]}")
