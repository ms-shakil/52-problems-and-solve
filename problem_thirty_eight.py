# Palindrome 
inp = input("Enter a  string :")
def MyFunction(inp):
    var = inp[::-1]
    if inp == var:
        print("yes! It is Palindrome !")
    else:
        print("sorry ! It is not Palindrome!")

MyFunction(inp)            