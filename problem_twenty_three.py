# Find array alternate elements
inp =[2,3,5,2,4,64,62,34,53,2,4,23,53,63]
def Myfunction(value):
    for i in range(1,len(value),2):
      print('{} {}'.format(" ",value[i]), end =" ")

Myfunction(inp)
