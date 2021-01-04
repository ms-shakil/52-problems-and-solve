var inp  = 5
function MyFunction(inp){
    for(var i = inp ; i > 0; i--){
        if(i >= 2){
             console.log(2,"^",i)
        }
        else{
            console.log("2+1 ")
        }
    }
}
MyFunction(inp)