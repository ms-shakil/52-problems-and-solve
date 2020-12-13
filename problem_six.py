value = input("enter the number:")
def Length(val):
    arr = len(val.split())
    return arr
print("There are have {}element. ".format(Length(value)))