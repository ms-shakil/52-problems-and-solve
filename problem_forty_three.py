#Pascal's triangle
inp = int(input("Enter the number:"))
def MyFunction(inp):
    lst =[]
    for i in range(inp): 
        lst2 =[]
        if i == 0:
            print(1)
            print(1,1)    
        elif i == 1:
            print(1,i+1,1)
            lst.append(1)
            lst.append(i+1)
            lst.append(1)
        elif i>1:
            for j in range(len(lst)-1):
                if j == 0:
                    lst2.append(1)
                    value = lst[j]+lst[j+1]
                    lst2.append(value)
                elif j >0:
                    val =lst[j]+lst[j+1]   
                    lst2.append(val)  
            lst2.append(1)
            listToStr = ' '.join([str(elem) for elem in lst2]) 
            print(listToStr)
            lst =lst2                
MyFunction(inp)









               

         


