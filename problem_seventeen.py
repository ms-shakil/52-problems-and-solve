# count vowels and consonants
inp = input("Enter a sentence:")
def MyFunction(inp):
    val = list(inp.replace(" ", ""))
    count = ""
    count1 =""
    for i in val:
        if i == "a" or i == "e" or i =="i" or i =="o" or i =="u":
            count += i
        else :
            count1+=i    
    print("Vowels -> ",count)
    print("Consonants ->",count1)
MyFunction(inp) 