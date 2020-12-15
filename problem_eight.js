// squre numbr check
var value = 64
function squreNumber(num){
    var sqr = Math.sqrt(num)
    var sq = Math.floor(sqr)
    if(sq*sq == value){
        console.log("yes")
    }
    if(sq*sq != value){
        console.log("no")
    }
}
squreNumber(value)


