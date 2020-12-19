# reverse string
value = input("Enter your name:")
def Myfunction(val):
    lst =list(val)[::-1]
    value ="".join(lst)
    print(value)

Myfunction(value)    