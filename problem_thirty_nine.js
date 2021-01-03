// The sum of the streams
var inp1 = 2
var inp2 = 5
function Myfunction(inp1,inp2){
    var count = 0
    for(var i =0 ;i< inp2 + 1; i++){
        var value = inp1**i
        count += value
    }
    return count

}
console.log(Myfunction(inp1,inp2))