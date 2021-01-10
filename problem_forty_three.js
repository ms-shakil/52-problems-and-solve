//Pascal's triangle
var value = 10
function MyFunction(value){
    var list =[]
    for(var i = 0;i<value;i++){
        var arr =[]
        if (i == 0){
            console.log(1)
            console.log(1,1)
            list.push(1)
            list.push(1)
        }
        else {
            for (var j = 0; j<list.length-1;j++){
                if(j ==0){
                    arr.push (1)
                    var val= list[j]+list[j+1]
                    arr.push(val)
                }else{
                    var valu=list[j]+list[j+1]
                    arr.push(valu)
                }
            }
            arr.push(1)
            for (var k=0; k<arr.length;k++){
                console.log(arr[k])
            }
            list =arr
        }
        
    
    }
    
}
MyFunction(value)