# Character check 
inp =input("Enter character:")
def Case_Check(inp):
    if inp >= "0" and inp <= "9":
        print("Numberical Character.")
    elif inp >= "a" and inp <="z":
        print("Lower Case Character.")
    elif inp >= "A" and inp <="Z":
        print("Upper Case Character.")
    else:
        print("Special Char")

Case_Check(inp)                    
