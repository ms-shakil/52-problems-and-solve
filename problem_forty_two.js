//Modular Exponentiation (Power in Modular Arithmetic)
var number = 2
var power = 10
var mod = 5
function myFunction(number,power,mod){
    var value = (number**power)%mod
    return value
}
console.log("Result = ",myFunction(number,power,mod))