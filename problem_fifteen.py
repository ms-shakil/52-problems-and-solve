# reverse text element
val ="hello payer bhai"
def Reverse(value):
    lst = value.split(" ")
    arr =[]
    for i in lst:
        arr.append(i[::-1])   
    listToStr = ' '.join([str(elem) for elem in arr])          
    return  listToStr
print(Reverse(val))       

