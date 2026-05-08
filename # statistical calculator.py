# statistical calculator
def mean(list):
    mean=(sum(list))/len(list)
    return mean

def mode(list):
    max_count=0
    max_item=0
    mode_list=[]
    for items in list:
        item_count=list.count(items)
        if item_count>max_count:
            max_count=item_count
            max_item=items
            previous_item=items
        elif item_count==max_count and items != max_item:
            if items != previous_item:
                if items not in mode_list:
                    if previous_item not in mode_list:
                        mode_list.append(previous_item)
                    mode_list.append(items)
            max_item=mode_list
    if max_count==1:
        max_item="No mode"
    return max_item

def median(list):
    sorted_list=sorted(list)
    if len(sorted_list) % 2 !=0:
        median=sorted_list[len(sorted_list)//2]
    else:
        median=(sorted_list[(len(sorted_list)//2)-1]+sorted_list[len(sorted_list)//2])/2
    return median

def basic_stats(list):
    mean_value=mean(list)
    mode_value=mode(list)
    median_value=median(list)
    return mean_value, mode_value, median_value

def standard_deviation(list):
    standard_deviation_sample="None"
    mean_value=mean(list)
    mean_difference_list=list.copy()
    for items in range(len(mean_difference_list)):
        mean_difference_list[items]=(abs(mean_difference_list[items]-mean_value))**2
    square_mean=mean(mean_difference_list)
    standard_deviation=square_mean**(0.5)
    if len(list)>1:
        sample_s_mean=sum(mean_difference_list)/(len(mean_difference_list)-1)
        standard_deviation_sample=sample_s_mean**(0.5)
    return standard_deviation, standard_deviation_sample

if __name__=="__main__":
    set=[85, 85, 90, 92, 95, 96, 97, 100, 103, 104, 105, 112, 115, 118, 135]
    user_stats=(basic_stats(set))
    user_mean, user_mode, user_median= user_stats
    print(f"The mean value of the set is {user_mean:.2f}, the mode of the set is {user_mode} and the median value of the set is {user_median}.")
    user_deviations=standard_deviation(set)
    user_standard, user_sample_standard=user_deviations
    print(f"The standard deviation of the set is {user_standard:.2f} and the sample standard deviation is {user_sample_standard:.2f}")  