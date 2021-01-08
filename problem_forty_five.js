//area of triangle
var inp1=13
var inp2 =18
var inp3 = 15
function myFunction(a,b,c){
    var s = (a+b+c)/2
    var area = Math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area.toFixed(3)
}
console.log("area =",myFunction(inp1,inp2,inp3))