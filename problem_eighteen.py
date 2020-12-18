# word count by input sentence
value = input("Enter the sentence:")
def MyFunction(val):
    value = val.split(" ")
    print("count = ",len(value))
MyFunction(value)
