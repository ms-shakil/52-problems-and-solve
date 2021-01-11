//find lost number
var inp= 10
var lst =[1,2,3,5,6,7,9,10]
function MyFunction(inp,lst){
    for (var i=1; i<inp+1;i++){
        var boll = true
        for(var j = 0 ;j<lst.length;j++){
            if(lst[j]==i){
                boll = false
            }
        }if(boll){
            console.log(i)
        }      
    }
}
MyFunction(inp,lst)