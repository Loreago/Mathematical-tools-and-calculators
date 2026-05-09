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

def correlation(set1: list,set2: list):
    mean_value_list1=mean(set1)
    mean_difference_list1=set1.copy()
    for items in range(len(mean_difference_list1)):
        mean_difference_list1[items]=mean_difference_list1[items]-mean_value_list1
    mean_value_list2=mean(set2)
    mean_difference_list2=set2.copy()
    for items in range(len(mean_difference_list2)):
        mean_difference_list2[items]=mean_difference_list2[items]-mean_value_list2
    covariance=0
    index=0
    for items in mean_difference_list1:
        covariance+= (mean_difference_list1[index])*(mean_difference_list2[index])
        index+=1
    sample_covariance=covariance/(len(mean_difference_list1)-1)
    covariance=covariance/len(mean_difference_list1)
    sd1=standard_deviation(set1)
    sd2=standard_deviation(set2)
    correlation=covariance/(sd1[0]*sd2[0])
    sample_correlation=sample_covariance/(sd1[1]*sd2[1])
    return correlation, sample_correlation


if __name__=="__main__":
    set1=[85, 85, 90, 92, 95, 96, 97, 100, 103, 104, 105, 112, 115, 118, 135]
    set2=[172.7, 172.7, 182.88, 170, 170, 172.7, 172.7, 175, 167.6, 154.9, 170, 185.42, 182.88, 170, 173.8]
    user_stats=(basic_stats(set1))
    user_mean, user_mode, user_median= user_stats
    print(f"The mean value of the set is {user_mean:.2f}, the mode of the set is {user_mode} and the median value of the set is {user_median}.")
    user_deviations=standard_deviation(set1)
    user_standard, user_sample_standard=user_deviations
    print(f"The standard deviation of the set is {user_standard:.2f} and the sample standard deviation is {user_sample_standard:.2f}")
    user_correlation=correlation(set1,set2)
    standard_correlation, sample_correlation=user_correlation
    print(f"The correlation between the two data sets is {standard_correlation:.3f} and the sample correlation is {sample_correlation:.3f}")
