#  Divisor number checking
inp = int(input("Enter The number:"))
for i in range(1,inp+1):
    if inp % i == 0:
        print( i)
    