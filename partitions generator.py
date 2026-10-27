partition_count=1
def recursive_partition(original_number: list):
    """A function that generates the partitions of a given number. Albeit, recursively"""
    global partition_count
    if len(original_number)==1 and original_number[0]==1:
        return original_number
    else:
        if len(original_number)==1:
            print(partition_print(original_number))
        index=-1
        main_number=sum(original_number)
        for number in original_number[::-1]:    
            partition_condition=False   
            if number==1:
                index-=1
                continue
            root_number=number-1
            new_partition=[]
            if index!=(-len(original_number)):
                new_partition=original_number[-len(original_number):index].copy()
            new_partition.append(root_number)
            while True:
                if sum(new_partition)+root_number==main_number:
                    new_partition.append(root_number)
                if sum(new_partition)+root_number<main_number:
                    new_partition.append(root_number)
                elif sum(new_partition)+root_number>main_number:
                    partition_condition=True
                    break
            if partition_condition==True:
                break
            index-=1
        if sum(new_partition)<main_number:
            for number in range(new_partition[-1],0,-1):
                if sum(new_partition)+number==main_number:
                    new_partition.append(number)
                    break
        partition_count+=1
        print(partition_print(new_partition))
        if len(new_partition)==new_partition.count(1):
            print("all partitions printed")
            return new_partition
        recursive_partition(new_partition)

def partition_print(partition: list):
    if len(partition)==1:
        return f"{partition[0]}"
    string=""
    index=0
    for number in partition:
        if index!=len(partition)-1:
            string+=str(number)+" + "
        else:
            string+=str(number)
        index+=1
    return string


def partition(original_number: list,printout: bool):
    """partition function that generates the next partition when given a number or partition. Does not use Recursion."""
    if len(original_number)==1 and original_number[0]==1:
        return original_number
    else:
        if len(original_number)==1:
            if printout==True:
                print(partition_print(original_number))
        index=-1
        main_number=sum(original_number)
        for number in original_number[::-1]:    
            partition_condition=False   
            if number==1:
                index-=1
                continue
            root_number=number-1
            new_partition=[]
            if index!=(-len(original_number)):
                new_partition=original_number[-len(original_number):index].copy()
            new_partition.append(root_number)
            while True:
                if sum(new_partition)+root_number==main_number:
                    new_partition.append(root_number)
                if sum(new_partition)+root_number<main_number:
                    new_partition.append(root_number)
                elif sum(new_partition)+root_number>main_number:
                    partition_condition=True
                    break
            if partition_condition==True:
                break
            index-=1
        if sum(new_partition)<main_number:
            for number in range(new_partition[-1],0,-1):
                if sum(new_partition)+number==main_number:
                    new_partition.append(number)
                    break
        if printout==True:
            print(partition_print(new_partition))
        if len(new_partition)==new_partition.count(1):
            print("All partitions printed/counted.")
    return new_partition

def partitions(number: int,printout: bool):
    partition_number=[]
    partition_number.append(number)
    partition_count=1
    while True:
        new_number=partition(partition_number,printout)
        partition_count+=1
        if len(new_number)==new_number.count(1):
            break
        partition_number=new_number
    return partition_count

if __name__=="__main__":
    partition_number=int(input("Enter the number whose partitions are to be generated/counted: "))
    prints_partition=input("Do you want the partitions to be printed? Not recommended for large numbers. Enter y/n: ")
    if prints_partition=="y":
        printout=True
    else:
        printout=False
    output=partitions(partition_number,printout)
    print(f"There are {output-1} partitions of {partition_number}. {output} partitions including itself.")