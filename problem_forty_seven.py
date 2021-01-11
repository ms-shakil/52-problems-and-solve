# find lost number
inp =10
lst=[2,3,5,1,6,8,9,10]
def MyFunction(inp,lst):
    for i in range(1,inp+1,1):
        bollen=False
        for j in range(len(lst)):
            if lst[j]==i:
                bollen= True
                break
        if bollen==False:
           print(i)

MyFunction(inp,lst)