// The sum of the streams 2
var inp = 8
function Myfunction(inp){
    var count = 0 
    for (var i = 0; i < inp; i++){
        var mult = 1
        for (var j = 0; j<i; j++){
            var add = j* mult
            mult+= add
        }
        var div = i/mult
        count += div
    }
    return count

}
console.log(Myfunction(inp))