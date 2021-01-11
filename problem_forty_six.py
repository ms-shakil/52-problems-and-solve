# two list item join and print sortly 
lst1 =[1458,5,4,86,86,56]
lst2=[6,8,97,56,4,3]
def Sort_list (lst1,lst2):
    value = lst1+lst2
    for i in range(len(value)):
        for j in range(i,len(value),1):
            if value[i]> value[j]:
                T = value[i]
                value[i]=value[j]
                value[j]=T

    return value            

print(Sort_list(lst1,lst2))