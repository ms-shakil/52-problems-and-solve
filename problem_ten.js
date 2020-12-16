// This code work for get factorial number.
var number = 100
function factorialNumber(number){
    var num = 1
    for(var i = 0;i < number;i++){
        var val = i*num
        num+=val
    }
    return num
}
console.log("This is factorial number:",factorialNumber(number))
