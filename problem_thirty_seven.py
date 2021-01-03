inp1 = int(input("enter the length:"))
inp2 = input("Enter the singal number:")
def MyFunction(inp,inp2):
    ind = 1
    while inp >= ind: 
        print(inp2*ind)
        ind+=1
        if inp == ind :
            while inp > 0:
                print(inp*inp2)
                inp -=1
                



MyFunction(inp1,inp2)
    
   


   