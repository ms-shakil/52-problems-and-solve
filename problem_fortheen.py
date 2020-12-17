# how many singal  caraacter have this sentence.
value= input("Enter a sentence:")
def Myfunction(data):
    val = data.replace(" ", "")
    lst = list(val)
    dic={}
    for i in lst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]= 1
    return dic
print(Myfunction(value))