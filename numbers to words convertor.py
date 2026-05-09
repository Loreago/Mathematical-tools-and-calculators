# numbers to words convertor
numberwords={0: "zero",1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
                 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 
                 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}  
def number_words(numbers):
    if numbers<21:
        number_in_words=numberwords[numbers]
    elif numbers % 10==0:
        number_in_words=numberwords[numbers]
    else:
        string=str(numbers)
        number_in_words=numberwords[(int(string[0])*10)]+"-"+numberwords[int(string[1])]
    return number_in_words

def powers_three(number):
    number_word=str(number)
    power_numbers={1: "thousand", 2: "million", 3: "billion", 4: "trillion", 
                   5: "Quadrillion", 6: "Quintillion", 7: "Sextillion", 
                   8: "Septillion",9: "Octillion", 10: "Nonillion", 11: "Decillion"}
    index=0
    counter=0
    final=""
    if number==0:
        final=number_words(number)
        return final
    while len(number_word)>0:
        power=len(number_word)
        power_by_threes=len(number_word)//3
        if len(number_word) % 3==0:
            power_by_threes-=1
        if number_word[0]=="0" and len(number_word)>0:
            number_word=number_word[0+1:]
            if len(number_word)==0:
                break
        if len(number_word) % 3==0 and int(number_word)!= 0 and number_word[0]!= "0":
            if power>3:
                final += number_words(int(number_word[0]))+" "+ "hundred "
            else:
                final += number_words(int(number_word[0]))+" "+ "hundred "
            number_word=number_word[1:]
        elif len(number_word) % 3==2 and int(number_word)!= 0 and number_word[0]!= "0":
            if power>3:
                final += number_words(int(number_word[0:2]))+" "
            else:
                final += number_words(int(number_word[0:]))+" "
            number_word=number_word[2:]
        elif len(number_word) % 3==1 and int(number_word)!= 0 and number_word[0]!= "0":
            final += number_words(int(number_word[0]))+" "
            number_word=number_word[1:]
        if power_by_threes in power_numbers and len(number_word) %3==0 and counter<1:
            if int(number_word)==0:
                counter=1
            if number_word[0]=="0":
                index1=0
                for digits in number_word:
                    if digits != 0:
                        non_zero_index=index
                    index1+=1
                if number_word[0: non_zero_index]=="0"*len(number_word[0:non_zero_index]):
                    counter=1
            final += power_numbers[power_by_threes]+" "
        index += 1
        power -= 1
    return final

if __name__=="__main__":
    print(powers_three(5750))