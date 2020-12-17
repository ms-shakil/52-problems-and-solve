# probability
Fruits =["apple","banana","blackcurrant","mango","apple","apple","banana","mango","mango","apple"]
data = input("Enter probability fruite name:")
def Fruits_prbability(list,fruit):
    list_len =len(list)
    count = 0
    for i in list:
        if i == fruit:
            count+=1
    probability = count/ list_len        
    return probability       
print(Fruits_prbability(Fruits,data))



