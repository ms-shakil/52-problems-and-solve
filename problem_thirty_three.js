
var inp = 5
var inp1 = 6
var inp2 = 100
function MyFunction(div1,div2,value){
    for(var i = 1; i < value; i++ ){
        var mod1 = i % div1
        var mod2 = i % div2
        if (mod1 == 0 && mod2==0){
            console.log(i)
        }
    }
}
MyFunction(inp,inp1,inp2)