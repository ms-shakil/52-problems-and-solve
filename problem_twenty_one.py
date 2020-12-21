# count prime number  from low to high number.
low = int(input("Enter low number:"))
high = int(input("Enter upper  number:"))

def MyFunction(low,high):
    count = 0
    for i in range(low,high+1):
        if i > 1:
            for j in range(2,i):
                if i%j== 0 :
                   break
            else:
               count+=1
    return count

print("count = ",MyFunction(low,high))             


    


                   


   
    
    


