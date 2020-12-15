# checking small number to large number
a = int(input("Enter the first number:"))
b=  int(input("Enter the second number:"))
c=  int(input("Enter the third number:"))
def smallnumber(a,b,c):
    if  a > b :
       T = a
       a = b
       b = T
    if a > c:
       J = a
       a= c
       c =J
    if  b > c:
       k = b
       b = c
       c =k
    print(a,b,c)

smallnumber(a,b,c)