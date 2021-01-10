#Pascal's triangle
inp = int(input("Enter the number:"))
def MyFunction(inp2):
    inp =5
    save_data =[]
    lst =[]
    for i in range(inp): 
        lst2 =[]
        if i == 0:
            print(1)
            print(1,1) 
            lst.append(1)
            lst.append(1)   
        elif i>0:
            for j in range(len(lst)-1):
                if j == 0:
                    lst2.append(1)
                    value = lst[j]+lst[j+1]
                    lst2.append(value)
                elif j >0:
                    val =lst[j]+lst[j+1]   
                    lst2.append(val)  
            lst2.append(1)
            save_data.append(lst2) 
            lst =lst2      
    if inp2 <= len(save_data)+1:
        for i in range(inp2-1):
            listToStr = ' '.join([str(elem) for elem in save_data[i]]) 
            print(listToStr)         
    else:
        for i in range(len(save_data)-1,inp2-2,1):
            lst2=[] 
            for j in range(len(save_data[i])-1):
                if j== 0:
                    lst2.append(1)              
                    value=save_data[i][j]+save_data[i][j+1]
                    lst2.append(value)
                else :
                    val = save_data[i][j]+save_data[i][j+1]
                    lst2.append(val)
            lst2.append(1)    
            save_data.append(lst2)  
        for i in save_data:
            listToStr = ' '.join([str(elem) for elem in i]) 
            print(listToStr)
                
MyFunction(inp)

