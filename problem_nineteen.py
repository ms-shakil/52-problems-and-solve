# word count by input somplex sentence;
import re
text = input("Enter text:")
def MyFunction(text):
    value = re.sub(r'[,.!]', ' ', text)
    val =" ".join(value.split())
    print("Count = ",len(val.split(" ")))

MyFunction(text)





