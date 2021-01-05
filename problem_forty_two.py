#Modular Exponentiation (Power in Modular Arithmetic)
inp =int(input("Enter the number:"))
power = int(input("Enter the power:"))
mod = int(input("Enter the mod:"))
def MyFunction(inp,power,mod):
    value = (inp**power)%mod
    return value

print("Result = ",MyFunction(inp,power,mod))    