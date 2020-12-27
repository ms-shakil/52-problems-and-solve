# check sorted list
arr = int(input("Enter list length:"))
def MyFunction(arr):
    lst =[]
    for i in range(0,arr,1):
       element = int(input("Enter list element:"))
       lst.append(element)
       count =1
    for i in range(0,len(lst)-1,1):
        if i < i+1:
            count+=1
        else :
            print("No this element not sorted.")
            break   
    if len(lst)== count:
        print("Yes this list element sorted")

MyFunction(arr)

