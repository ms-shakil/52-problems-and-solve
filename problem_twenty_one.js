// count prime  from low to high
var low = 10
var high = 50
function myFunction(low,high){
    var count = 0
    for (var i = low ; high+1 > i ; i++){
        var  val = true
        if(i >1){
            for(var j = 2 ; i > j;j++){
                if( i% j===0){
                    val  = false
                    break           
                }     
            }
            if(val){
               count+=1
            }            
        }  
    }
    return count  
}
console.log(myFunction(low,high))
