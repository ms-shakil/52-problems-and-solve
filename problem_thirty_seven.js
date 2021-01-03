var inp = 5
var inp1  = "*"
function MyFunction(inp,inp1){
    var val = 1
    while (inp >= val){
        console.log(inp1*val)
        val +=1
    }if (inp == val){
        while (inp > 0){
            console.log(inp1* inp)
            inp -=1
        }
    }
}
MyFunction(inp,inp1)