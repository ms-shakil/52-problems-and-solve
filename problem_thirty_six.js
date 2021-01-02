// reverse a number
var inp = 3435455656
function Myfunction(inp){
    var val =parseInt(String(inp).split("").reverse().join(""))
    console.log(val)
}
Myfunction(inp)