// Find the number of zeros at the end of the factorial number
var number = 15
function fun(){
    var num = 1
    for(var i = 0;i < number;i++){
        var val = i*num
        num+=val
    }
    var arr = String(num).split("")
    var count = 0
    for(var i = arr.length -1; i > 0;i--){
        if (parseInt(arr[i])== 0){
            count+=1
        }
        if(parseInt(arr[i])!=0){
            break
        }
    }
    return count
}
console.log(fun(number))