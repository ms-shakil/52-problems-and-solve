// Multiplier inp1 to inp2
var inp1 = 2
var inp2 = 10
function Multiplier(inp1,inp2){
    if (inp1 < inp2){
       var count  = 0
        var range = 1
        while(count <= inp2){
            var value =  inp1*range
            if(value <= inp2){
                console.log(value)
            }
            count = value
            range+=1
        }
    }else{
        console.log("invalid")
    }
    }
  
Multiplier(inp1,inp2)
