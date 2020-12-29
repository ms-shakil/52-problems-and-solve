var inp = 55
var inp2 = 100
var inp3 = 6
function Myfunction(lower,upper,divi){
    for(var i = lower; i < upper; i++){
        val = i % divi
        if (val == 0){
            console.log(i)
        }
    }
}
Myfunction(inp,inp2,inp3)