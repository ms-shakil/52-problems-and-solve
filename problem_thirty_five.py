# string sort
import re
sentence = input("Enter the sentence:")
def MyFunction(value):
    val =re.sub(r'[,.!]', ' ', value)
    vals =" ".join(val.split())
    lst = vals.split(" ")
    x =sorted(lst)
    for i in x:
        print(i)

MyFunction(sentence)

