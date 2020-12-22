# String to number.
value = input("Enter string:")
def StrToNumber(value):
    val = list(value)
    data = []
    for i in val:
        if i=="A" :
            i = 1
        elif i == "B" :
            i = 2
        elif i == "C" :
            i = 3
        elif i == "D":
            i = 4 
        elif i == "E":
            i = 5
        elif i == "F" :
            i = 6
        elif i == "G":
            i = 7    
        elif i == "H":
            i = 8
        elif i == "I":
            i = 9
        elif i == "J":
            i =10
        elif i == "k":
            i = 11
        elif i == "L":
            i = 12
        elif i == "M" :
            i =13
        elif i == "N" :
            i =14
        elif i == "O":
            i =15
        elif i == "P" :
            i =16
        elif i == "Q" :
            i =17
        elif i == "R" :
            i =18
        elif i == "S" :
            i =19
        elif i == "T" :
            i =20
        elif i == "U" :
            i =21
        elif i == "V":
            i =22
        elif i == "W" :
            i =23
        elif i == "X":
            i =24
        elif i == "Y":
            i =25
        elif i == "Z" :
            i =26   
         
        else:
            print("Input shoud Uppercase.")
            break
        data.append(str(i))      
    print("".join(data)) 

StrToNumber(value)
